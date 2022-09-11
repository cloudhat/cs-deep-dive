package lecture05;

class Node {
    int data;
    Node left;
    Node right;

    int height;

    public Node(int data) {
        this.data = data;
    }
}

public class avl {

    private int height(Node node) {
        return node != null ? node.height : -1;
    }

    private void updateHeight(Node node) {
        int leftChildHeight = height(node.left);
        int rightChildHeight = height(node.right);

        node.height = 1 + Math.max(leftChildHeight, rightChildHeight);
    }

    private int balanceFactor(Node node) { // 절댓값 1을 넘어갈시 AVL이 아님
        return height(node.right) - height(node.left);
    }

    private Node rotateRight(Node node) {
        // https://www.happycoders.eu/wp-content/uploads/2021/08/avl-tree-right-rotation-1200x342.png

        Node leftChild = node.left;

        node.left = leftChild.right;
        leftChild.right = node;

        updateHeight(node);
        updateHeight(leftChild);

        return leftChild; // 새로운 루트가 된 leftChild
    }

    private Node rotateLeft(Node node) {
        // https://www.happycoders.eu/wp-content/uploads/2021/08/avl-tree-left-rotation-v2-1200x342.png

        Node rightChild = node.right;

        node.right = rightChild.left;
        rightChild.left = node;

        updateHeight(node);
        updateHeight(rightChild);

        return rightChild;
    }

    /*
     * - left-heavy 리밸런싱 :
     * - rotateRight
     * - left-right rotation
     * - right-heavy 리밸런싱 :
     * - rotateLeft
     * - right-left rotation
     */

    private Node rebalance(Node node) { // avl 회복
        int balanceFactor = balanceFactor(node); // height(node.right) - height(node.left);

        // left heavy
        if (balanceFactor < -1) {
            if (balanceFactor(node.left) <= 0) { // 왼쪽으로 이어지는 형태
                node = rotateRight(node);
            } else { // 왼쪽밑 -> 오른쪽밑
                node.left = rotateLeft(node.left);
                node = rotateRight(node);
            }
        }

        // right heavy
        if (balanceFactor > 1) {
            if (balanceFactor(node.right) > 0) { // 우측으로 이어지는 형태
                node = rotateLeft(node);
            } else { // 우측 밑 -> 왼쪽 밑
                node.right = rotateRight(node.right);
                node = rotateLeft(node);
            }
        }

        return node;
    }

    private Node basicInsert(int key, Node node) {
        if (node == null) {
            node = new Node(key);
        }

        else if (key < node.data) {
            node.left = insertNode(key, node.left);
        } else if (key > node.data) {
            node.right = insertNode(key, node.right);
        } else {
            throw new IllegalArgumentException("BST already contains a node with key " + key);
        }

        return node;
    }

    private Node insertNode(int key, Node node) {
        node = basicInsert(key, node);

        updateHeight(node);

        return rebalance(node);
    }
}
