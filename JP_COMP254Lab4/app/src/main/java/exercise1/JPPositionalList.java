package exercise1;

import java.util.Iterator;

import lists.Position;
import lists.PositionalList;

public interface JPPositionalList<E> extends PositionalList<E> {
    default int indexOf(Position<E> p) {
        int i = 0;
        Iterator<Position<E>> it = positions().iterator();
        while (it.hasNext()) {
            Position<E> current = it.next();

            if (current.equals(p))
                return i;

            i++;
        }
        return -1;
    }
}
