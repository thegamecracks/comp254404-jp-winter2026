package exercise3;

import queues.LinkedQueue;

public class Exercise3 {
    public static void main(String[] args) {
        LinkedQueue<Integer> a = new LinkedQueue<>();
        a.enqueue(1);
        a.enqueue(2);
        a.enqueue(3);
        a.enqueue(4);

        LinkedQueue<Integer> b = new LinkedQueue<>();
        b.enqueue(5);
        b.enqueue(6);
        b.enqueue(7);
        b.enqueue(8);

        System.out.printf("Queue A: %s\n", a);
        System.out.printf("Queue B: %s\n", b);

        a.concatenate(b);

        System.out.println("After concatenation:");
        System.out.printf("Queue A: %s\n", a);
        System.out.printf("Queue B: %s\n", b);
    }
}
