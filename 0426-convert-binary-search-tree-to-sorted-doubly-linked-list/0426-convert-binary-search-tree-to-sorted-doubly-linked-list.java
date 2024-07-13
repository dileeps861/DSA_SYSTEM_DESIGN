/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val,Node _left,Node _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/

class Solution {
    Node dummy = null;
    Node head = null;
    private void inorder(Node node){
        if(node == null){
            return;
        }
        inorder(node.left);
        Node newNode = new Node(node.val);
        newNode.left = dummy;
        dummy.right = newNode;
        dummy = newNode;
        inorder(node.right);
    }
    public Node treeToDoublyList(Node root) {
        if(root == null){
            return null;
        }
        dummy = new Node(0);
        head = dummy;

        inorder(root);
        dummy.right = head.right;
        head.right.left = dummy;
        // while(dummy != null){
        //     System.out.println(dummy.val);
        //     System.out.println("Is right:");
        //     dummy = dummy.right;
        // }
        return head.right;
    }
}