import networkx as nx
from matplotlib import pyplot as plt
import japanize_matplotlib

##  共起ネットワークを表示する関数
def plot_network(data, edge_threshold=0., fig_size=(15, 15), save_path='', edge_weight=3):

    nodes = list(set(data['node1'].tolist()+data['node2'].tolist()))

    G = nx.Graph()
    #  頂点の追加
    G.add_nodes_from(nodes)

    #  辺の追加
    #  edge_thresholdで枝の重みの下限を定めている
    for i in range(len(data)):
        row_data = data.iloc[i]
        if row_data['value'] > edge_threshold:
            G.add_edge(row_data['node1'], row_data['node2'], weight=row_data['value'])

    # 孤立したnodeを削除
    isolated = [n for n in G.nodes if len([i for i in nx.all_neighbors(G, n)]) == 0]
    for n in isolated:
        G.remove_node(n)

    plt.figure(figsize=fig_size, facecolor='w')
    pos = nx.spring_layout(G, k=0.3, iterations=20)  # k = node間反発係数

    pr = nx.pagerank(G)

    # nodeの大きさ
    nx.draw_networkx_nodes(G, pos, node_color=list(pr.values()),
                           cmap=plt.cm.Reds,
                           alpha=0.7,
                           node_size=[50000*v for v in pr.values()])

    # 日本語ラベル
    nx.draw_networkx_labels(G, pos, font_size=14, font_family='IPAexGothic', font_weight="bold")

    # エッジの太さ調節
    edge_width = [(d["weight"]-edge_threshold) * edge_weight for (u, v, d) in G.edges(data=True)]
    nx.draw_networkx_edges(G, pos, alpha=0.4, edge_color="darkgrey", width=edge_width)

    plt.axis('off')
    if save_path:
      plt.savefig(save_path, bbox_inches="tight")