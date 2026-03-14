package exercises;

import static org.junit.jupiter.api.Assertions.*;

import java.util.Iterator;

import org.junit.jupiter.api.Test;

import lists.LinkedPositionalList;
import lists.Position;
import lists.PositionalList;

class Exercise1Test {
    @Test void testPositionalListIndexOf() {
        PositionalList<String> list = new LinkedPositionalList<>();
        list.addLast("a");
        list.addLast("b");
        list.addLast("c");
        list.addLast("d");

        Iterator<Position<String>> it = list.positions().iterator();
        int index = 0;
        while (it.hasNext()) {
            Position<String> p = it.next();
            assertEquals(list.indexOf(p), index);
            index++;
        }
    }
}
