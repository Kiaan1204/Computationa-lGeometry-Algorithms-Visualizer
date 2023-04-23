import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_voronoi(voronoi):
    fig, ax = plt.subplots()

    def init():
        ax.set_xlim(min(voronoi.points[:, 0]) - 1, max(voronoi.points[:, 0]) + 1)
        ax.set_ylim(min(voronoi.points[:, 1]) - 1, max(voronoi.points[:, 1]) + 1)
        return []

    def update(frame):
        ax.clear()
        init()

        for i, region in enumerate(voronoi.regions[:frame]):
            if not -1 in region:
                polygon = [voronoi.vertices[i] for i in region]
                ax.fill(*zip(*polygon), alpha=0.4)

        ax.plot(voronoi.points[:frame, 0], voronoi.points[:frame, 1], 'ko')
        return []

    ani = animation.FuncAnimation(fig, update, frames=len(voronoi.regions), init_func=init, blit=True, interval=500)
    plt.show()
