package xyz.thegamecracks.comp254.lab6;

import xyz.thegamecracks.comp254.lab6.maps.SortedTableMap;

public class Exercise2 {
    public static void main(String[] args) {
        SortedTableMap<Integer, String> map = new SortedTableMap<>();

        System.out.printf("Does map contain 123? %s\n", map.containKey(123));
        System.out.printf("What is the value at 123? %s\n", map.get(123));
        System.out.println();

        map.put(123, "Hello world!");
        System.out.printf("Added 'Hello world!' at key 123\n");
        System.out.printf("Does map contain 123? %s\n", map.containKey(123));
        System.out.printf("What is the value at 123? %s\n", map.get(123));
        System.out.println();

        System.out.printf("Replaced '%s' with null\n", map.put(123, null));
        System.out.printf("Does map contain 123? %s\n", map.containKey(123));
        System.out.printf("What is the value at 123? %s\n", map.get(123));
        System.out.println();

        System.out.printf("Removed '%s' at key 123\n", map.remove(123));
        System.out.printf("Does map contain 123? %s\n", map.containKey(123));
        System.out.printf("What is the value at 123? %s\n", map.get(123));
        System.out.println();
    }
}
