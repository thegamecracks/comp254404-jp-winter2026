package exercise1;

import java.util.Iterator;

import lists.Position;

public class Exercise1 {
    public static void main(String[] args) {
        JPLinkedPositionalList<String> list = new JPLinkedPositionalList<>();

        list.addLast("a");
        list.addLast("b");
        list.addLast("c");
        list.addLast("d");
        System.out.println(list);

        Iterator<Position<String>> it = list.positions().iterator();
        while (it.hasNext()) {
            Position<String> p = it.next();
            System.out.printf("%s is at index: %d%n", p.getElement(), list.indexOf(p));
        }
    }
}
