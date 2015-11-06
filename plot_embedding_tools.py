
import numpy as np
import pylab as plt
from sklearn.decomposition import PCA


def annotate(syms, vecs, pl_ax, text_size=None, color='b'):
    print '# of syms:', len(syms)
    print vecs.shape
    for i, sym in enumerate(syms):
        xy = vecs[i, :]
        if text_size is None:
            text_size = 'x-small'
        pl_ax.annotate(sym, xy=xy, xytext=(-3, 2),
                       textcoords = 'offset points', size=text_size, color=color)


def plot_vec(vecs, syms, highlight_syms=None,
             highlight_only=False, doPCA=True,
             tag=''):

    if doPCA:
        pca = PCA(n_components=2)
        vecs = pca.fit_transform(vecs)
        print '=== PCA projection ==='
        print pca.explained_variance_ratio_
        print 'choosen explained: %.2f' % np.sum(pca.explained_variance_ratio_[:2])
    else:
        assert vecs.shape[1] == 2

    plt.scatter(vecs[:, 0], vecs[:, 1], s=10, color='b')

    ax = plt.gca()
    if not highlight_only:
        annotate(syms, vecs, ax)

    if highlight_syms is not None:
        highlight_vecs = []
        for sym in highlight_syms:
            if sym in syms:
                highlight_vecs.append(vecs[syms.index(sym), :])
        highlight_dot_sizes = 50
        color = 'r'
        highlight_vecs = np.asarray(highlight_vecs)
        plt.scatter(highlight_vecs[:, 0], highlight_vecs[:, 1],
                    s=highlight_dot_sizes, color=color)
        annotate(highlight_syms, highlight_vecs, ax, color=color)

    plt.title('chord space')
    plt.tick_params(axis='both', which='major', labelsize=6)

    plt.savefig('%s-%s.pdf' % ('chord_space', tag))

    # plt.show()