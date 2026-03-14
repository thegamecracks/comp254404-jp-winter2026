package exercises;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import queues.LinkedQueue;

class Exercise3Test {
    private LinkedQueue<Integer> a;
    private LinkedQueue<Integer> b;

    @BeforeEach
    void setUp() throws Exception {
        a = new LinkedQueue<>();
        a.enqueue(1);
        a.enqueue(2);
        a.enqueue(3);
        a.enqueue(4);

        b = new LinkedQueue<>();
        b.enqueue(5);
        b.enqueue(6);
        b.enqueue(7);
        b.enqueue(8);
    }

    @Test void testLinkedQueueConcatenate() {
        a.concatenate(b);
        assertEquals(a.size(), 8);
        assertEquals(b.size(), 0);

        for (int i = 1; i <= 8; i++) {
            assertEquals(a.dequeue(), i);
        }
    }
}
