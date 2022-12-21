import matplotlib.pyplot as plt
import subprocess
import argparse
import sys
import numpy as np

from IPython.core.magic import Magics, line_cell_magic, magics_class


# @register_line_magic
# def init_env(args):
def init_env(ip):
    """Use pip from the current kernel"""
    import tensorflow as tf
    from pip import main
    import matplotlib.pyplot as plt

    ip.os.system("apt-get install -y xvfb python-opengl")
    ip.os.system("pip install gymnasium pyvirtualdisplay gymnasium[atari,toy_text,box2d]")

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


@magics_class
class RLPlugin(Magics):
    def __init__(self, shell):
        super(RLPlugin, self).__init__(shell)
        self.argparser = argparse.ArgumentParser(description="ipsa_compile_and_exec params")
        self.argparser.add_argument(
            "-t", "--timeit", action="store_true", help="flag to return timeit result instead of stdout"
        )
        self.argparser.add_argument("-c", "--compiler", default="nvcc", choices=["nvcc", "g++", "gcc"])

    @line_cell_magic
    def rl_init(self, line, cell="", local_ns=None):
        try:
            args = self.argparser.parse_args(line.split())
        except SystemExit as e:
            self.argparser.print_help()
            return
        subprocess.check_output("ls -1".split(), stderr=subprocess.STDOUT)


def plot_environment(env, figsize=(5, 4)):
    plt.figure(figsize=figsize)
    img = env.render()
    if type(img) == list:
        img = img[0]
    plt.imshow(img)
    plt.axis("off")
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
    obs, info = env.reset(seed=seed)
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