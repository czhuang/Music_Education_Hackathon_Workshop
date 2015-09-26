
import numpy as np
import pylab as plt
from sklearn.decomposition import PCA


def annotate(syms, vecs, pl_ax, is_3d, text_size=None):
    print '# of syms:', len(syms)
    print vecs.shape
    for i, sym in enumerate(syms):
        xy = vecs[i, :]
        if text_size is None:
            text_size = 'small'
        pl_ax.annotate(sym, xy=xy, xytext=(-3, 2),
                       textcoords = 'offset points', size=text_size, color='b')


def plot_vec(vecs, syms, highlight_syms=None,
             highlight_only=False, doPCA=True):

    if doPCA:
        pca = PCA(n_components=2)
        vecs = pca.fit_transform(vecs)
        print '=== PCA projection ==='
        print pca.explained_variance_ratio_
        print 'choosen explained: %.2f' % np.sum(pca.explained_variance_ratio_[:2])
    else:
        assert vecs.shape[1] == 2

    plt.scatter(vecs[:, 0], vecs[:, 1], s=10, color='b')

    if highlight_syms is not None:
        pass
        # plt.scatter(highlight_vecs[:, 0], highlight_vecs[:, 1],
        #             s=highlight_dot_sizes, color='k')
        # annotate(highlight_syms, highlight_vecs, ax, False)

    ax = plt.gca()
    if not highlight_only:
        annotate(syms, vecs, ax, False)

    plt.title('chord space')
    plt.tick_params(axis='both', which='major', labelsize=6)

    plt.savefig('%s.pdf' % 'chord_space.pdf')

    # plt.show()