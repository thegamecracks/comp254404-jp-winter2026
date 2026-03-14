package exercises;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import exercise2.Exercise2;
import stacks.ArrayStack;
import stacks.LinkedStack;
import stacks.Stack;

class Exercise2Test {
    private Stack<Integer> a;
    private Stack<Integer> b;

    @BeforeEach
    void setUp() throws Exception {
        a = new LinkedStack<>();
        a.push(1);
        a.push(2);
        a.push(3);
        a.push(4);

        b = new ArrayStack<>();
        b.push(5);
        b.push(6);
        b.push(7);
        b.push(8);
    }

    @Test void testStackTransfer() {
        Exercise2.transfer(a, b);
        assertEquals(a.size(), 0);
        assertEquals(b.size(), 8);
        assertEquals(a.toString(), "()");
        assertEquals(b.toString(), "(1, 2, 3, 4, 8, 7, 6, 5)");
    }
}
