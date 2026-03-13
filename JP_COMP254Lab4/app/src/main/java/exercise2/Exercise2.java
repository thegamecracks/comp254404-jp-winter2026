package exercise2;

import stacks.ArrayStack;
import stacks.LinkedStack;
import stacks.Stack;

public class Exercise2 {
    public static void main(String[] args) {
        Stack<Integer> a = new LinkedStack<>();
        a.push(1);
        a.push(2);
        a.push(3);
        a.push(4);

        Stack<Integer> b = new ArrayStack<>();
        b.push(5);
        b.push(6);
        b.push(7);
        b.push(8);

        System.out.printf("Stack A: %s\n", a);
        System.out.printf("Stack B: %s\n", b);

        transfer(a, b);

        System.out.println("After transfer:");
        System.out.printf("Stack A: %s\n", a);
        System.out.printf("Stack B: %s\n", b);
    }

    private static <E> void transfer(Stack<E> s, Stack<E> t) {
        while (!s.isEmpty()) t.push(s.pop());
    }
}
