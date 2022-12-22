import matplotlib as mpl
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import collections

mpl.rc("animation", html="jshtml")


def record_scenario(env, policy, num_frames=100) -> dict:
    frames = []
    obs_mat = np.empty((num_frames, 4))
    actions = np.empty((num_frames,))
    rewards = np.empty((num_frames,))
    dones = np.empty((num_frames,), dtype=int)
    first_done_info = ""
    obs, info = env.reset()  # initial observation
    for i in range(num_frames):
        action = policy(obs)
        obs, reward, done, truncated, info = env.step(action)
        img = env.render()
        frames.append(img)
        obs_mat[i, :] = obs
        actions[i] = action
        rewards[i] = reward
        dones[i] = int(done)
        if done and first_done_info == "":
            first_done_info = info
    record = {
        "frames": frames,
        "obs": obs_mat,
        "actions": actions,
        "rewards": rewards,
        "dones": dones,
        "first_done_info": first_done_info,
    }
    return record


def update_scene(num, frames, patch, time_text, obs_mat, actions, cum_rewards, dones):
    patch.set_data(frames[num])
    text = f"frame: {num}"
    text += ", Obs: ({:.3f}, {:.3f}, {:.3f}, {:.3f})\n".format(*obs_mat[num, :])
    text += f"Action: {actions[num]}"
    text += f", Cumulative Reward: {cum_rewards[num]}"
    text += f", Done: {dones[num]}"
    time_text.set_text(text)
    return patch, time_text


def plot_animation(record, repeat=False, interval=40):
    """record should contain
    frames: list of N frames
    obs: (N, 4) array of observations
    actions: (N, ) array of actions {0, 1}
    rewards: (N, ) array of rewards at each step {0, 1}
    dones: (N, 1) array of dones {0, 1}
    """
    cum_rewards = np.cumsum(record["rewards"])
    frames = record["frames"]
    fig = plt.figure()
    patch = plt.imshow(record["frames"][0])
    ax = plt.gca()
    time_text = ax.text(0.0, 0.95, "", horizontalalignment="left", verticalalignment="top", transform=ax.transAxes)
    plt.axis("off")
    anim = animation.FuncAnimation(
        fig,
        update_scene,
        fargs=(frames, patch, time_text, record["obs"], record["actions"], cum_rewards, record["dones"]),
        frames=len(frames),
        repeat=repeat,
        interval=interval,
    )
    plt.close()
    return anim


# position, velocity, angle, angular velocity
CPObs = collections.namedtuple("CartPole_obs", "x v theta omega")


def make(*kargs, seed=42, **kwargs):
    import gymnasium as gym

    env = gym.make(*kargs, **kwargs)
    env.reset(seed=seed)
    return env
