import matplotlib.pyplot as plt
import sys
import numpy as np


def runrealcmd(command, verbose=True):
    from subprocess import Popen, PIPE, STDOUT

    process = Popen(command, stdout=PIPE, shell=True, stderr=STDOUT, bufsize=1, close_fds=True)
    if verbose:
        for line in iter(process.stdout.readline, b""):
            print(line.rstrip().decode("utf-8"))
    process.stdout.close()
    process.wait()


def init_env(ip):
    """Use pip from the current kernel"""
    import tensorflow as tf

    runrealcmd("apt-get install -y xvfb python-opengl", verbose=True)
    runrealcmd("pip install gymnasium pyvirtualdisplay array2gif", verbose=True)
    runrealcmd("pip install gymnasium[atari,toy_text,box2d,classic_control,accept-rom-license]", verbose=True)

    if not tf.config.list_physical_devices("GPU"):
        print("No GPU was detected. Neural nets can be very slow without a GPU.")
        if "google.colab" in sys.modules:
            print("Go to Runtime > Change runtime and select a GPU hardware accelerator.")
        if "kaggle_secrets" in sys.modules:
            print("Go to Settings > Accelerator and select GPU.")

    plt.rc("font", size=14)
    plt.rc("axes", labelsize=14, titlesize=14)
    plt.rc("legend", fontsize=14)
    plt.rc("xtick", labelsize=10)
    plt.rc("ytick", labelsize=10)
    plt.rc("animation", html="jshtml")


def plot_environment(env, figsize=(5, 4)):
    plt.figure(figsize=figsize)
    img = env.render()
    if type(img) == list:
        img = img[0]
    plt.imshow(img)
    plt.axis("off")
    plt.show()
    return img


def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    from pathlib import Path

    IMAGES_PATH = Path() / "images" / "rl"
    IMAGES_PATH.mkdir(parents=True, exist_ok=True)

    path = IMAGES_PATH / f"{fig_id}.{fig_extension}"
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)


def update_scene(num, frames, patch):
    patch.set_data(frames[num])
    return (patch,)


def plot_animation(frames, repeat=False, interval=40):
    import matplotlib

    fig = plt.figure()
    patch = plt.imshow(frames[0])
    plt.axis("off")
    anim = matplotlib.animation.FuncAnimation(
        fig, update_scene, fargs=(frames, patch), frames=len(frames), repeat=repeat, interval=interval
    )
    plt.close()
    return anim


def show_one_episode(policy, n_max_steps=200, seed=42):
    import gymnasium as gym

    frames = []
    env = gym.make("CartPole-v1", render_mode="rgb_array")
    np.random.seed(seed)
    obs, _ = env.reset(seed=seed)
    for step in range(n_max_steps):
        frames.append(env.render())
        action = policy(obs)
        obs, reward, done, truncated, info = env.step(action)
        if done or truncated:
            break
    env.close()
    return plot_animation(frames)


def basic_policy(obs):
    angle = obs[2]
    return 0 if angle < 0 else 1


def play_one_step(env, obs, model, loss_fn):
    import tensorflow as tf

    with tf.GradientTape() as tape:
        left_proba = model(obs[np.newaxis])
        action = tf.random.uniform([1, 1]) > left_proba
        y_target = tf.constant([[1.0]]) - tf.cast(action, tf.float32)
        loss = tf.reduce_mean(loss_fn(y_target, left_proba))

    grads = tape.gradient(loss, model.trainable_variables)
    obs, reward, done, truncated, info = env.step(int(action))
    return obs, reward, done, truncated, grads
