
class Node{
    int value;
    Node next;
    //constructor
    public Node(int value){
        this.value = value;
        this.next = null;
    }
}
public class Main {
    public static void main(String[] args) {
       // Create a linked list with 12,3,5,2
        Node head = new Node(12);
        head.next = new Node(3);
        head.next.next = new Node(5);
        head.next.next.next = new Node(2);
        System.out.println("--problem 2--");
        doIt(head);

        // problem 3
        // output doIt2(1), doIt2(3), doIt2(6)
        System.out.println("--problem 3--");
        System.out.println(doIt2(1));
        System.out.println(doIt2(3));
        System.out.println(doIt2(6));

        // problem 4
        System.out.println("--problem 4--");
        Node_db head2= new Node_db(2);
        head2 = addNode(head2, 4);
        head2 = addNode(head2, 8);
        head2 = addNode(head2,10);
        head2 = addNode(head2, 15);
        head2 = addNode(head2, 29);
        head2 = addNode(head2, 41);

        System.out.println(sumOfMiddleThree(head2));


    }
    public static void doIt(Node node){
        if (node == null){
            return;
        }
        doIt(node.next);
        System.out.println(node.value);
    }
    public static int doIt2(int num){
        if(num == 0){
            return 1;
        }else if(num == 1){
            return 1;
        }else if(num == 2){
            return 2;
        }else{
            return doIt2(num-1) + doIt2(num-2)-doIt2(num-3);
        }
    }

    //function to add nodes to the doubly linked list
    // head = addNode(head, value);
    public static Node_db addNode(Node_db head, int value){
        // create a new node
        Node_db newNode = new Node_db(value);
        // if this head is null
        if(head == null){
            return newNode;
        }
        //find the last node
        Node_db currentNode = head;
        while (currentNode.next != null){
            currentNode = currentNode.next;
        }
        // add the node to the list
        currentNode.next = newNode;
        newNode.prev = currentNode;
        return head;

    }

    //  find the sum of the three middle nodes
    public static int sumOfMiddleThree(Node_db head){
        // use two indics to point to the middle
        Node_db fast = head;
        Node_db slow = head;
        while (fast != null && fast.next != null){
            fast = fast.next.next;
            slow = slow.next;
        }
        // at present, the slow is pointing to the middle node
        return slow.value + slow.next.value + slow.prev.value;

    }
}