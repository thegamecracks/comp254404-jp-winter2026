package exercise1;

import java.util.Iterator;

import lists.PositionalList;

public interface JPPositionalList<E> extends PositionalList<E> {
    default int indexOf(E e) {
        int i = 0;
        Iterator<E> it = iterator();
        while (it.hasNext()) {
            E current = it.next();

            if (current.equals(e))
                return i;

            i++;
        }
        return -1;
    }
}
