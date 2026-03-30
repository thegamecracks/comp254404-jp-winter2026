package exercise3;

import java.util.Iterator;

import queues.Entry;
import queues.HeapPriorityQueue;
import queues.PriorityQueue;

public class Exercise3 {
    public static void main(String[] args) {
        PriorityQueue<String, String> pq = new UpheapHeapPriorityQueue<>();
        pq.insert("D", "D4");
        pq.insert("E", "E4");
        pq.insert("G", "G4");
        pq.insert("C", "C3");
        pq.insert("F", "F3");
        pq.insert("I", "I3");
        pq.insert("J", "J3");
        pq.insert("B", "B2");
        pq.insert("H", "H2");
        pq.insert("A", "A1");

        System.out.println(pq);

        while (!pq.isEmpty()) {
            Entry<String, String> entry = pq.removeMin();
            System.out.printf("%s => %s\n", entry.getKey(), entry.getValue());
        }
    }
}

class UpheapHeapPriorityQueue<K, V> extends HeapPriorityQueue<K, V> {
    @Override
    protected void upheap(int j) {
        if (j < 1) // we're at the root, can't move any higher
            return;

        int p = parent(j);
        if (compare(heap.get(j), heap.get(p)) >= 0)
            return;

        swap(j, p);
        upheap(p);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder("{");
        Iterator<Entry<K, V>> it = heap.iterator();

        while (it.hasNext()) {
            Entry<K, V> entry = it.next();
            sb.append(String.format("%s: %s", entry.getKey(), entry.getValue()));
            if (it.hasNext())
                sb.append(", ");
        }

        sb.append("}");
        return sb.toString();
    }
}
