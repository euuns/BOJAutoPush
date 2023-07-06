import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        Tree tree = new Tree();

        for (int i = 0; i < N; i++) {
            String treeMake = br.readLine();
            StringTokenizer tokenizer = new StringTokenizer(treeMake, " ");
            tree.addNode(tokenizer.nextToken(), tokenizer.nextToken(), tokenizer.nextToken());
        }

        tree.preOrder(tree.root);
        System.out.println();
        tree.inOrder(tree.root);
        System.out.println();
        tree.postOrder(tree.root);
    }
}

class Node{
    String data;
    Node right;
    Node left;

    public Node(String data){
        this.data = data;
    }
}

class Tree{
    Node root;

    public void addNode(String mid, String left, String right){
        if(root == null){
            if(!mid.equals("."))
                root = new Node(mid);
            if(!left.equals("."))
                root.left = new Node(left);
            if(!right.equals("."))
                root.right = new Node(right);
        }
        else{
            search(root, mid, left, right);
        }
    }

    public void search(Node root, String mid, String left, String right){
        if(root == null) return;
        if(root.data.equals(mid)){
            if(!left.equals("."))
                root.left = new Node(left);
            if(!right.equals("."))
                root.right = new Node(right);
        }
        else{
            search(root.left, mid, left, right);
            search(root.right, mid, left, right);
        }
    }

    public void preOrder(Node root) {
        if (root != null) {
            System.out.print(root.data);
            preOrder(root.left);
            preOrder(root.right);
        }
    }

    public void inOrder(Node root) {
        if (root != null) {
            inOrder(root.left);
            System.out.print(root.data);
            inOrder(root.right);
        }
    }

    public void postOrder(Node root) {
        if (root != null) {
            postOrder(root.left);
            postOrder(root.right);
            System.out.print(root.data);
        }
    }
}
