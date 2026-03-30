package exercise2;

import trees.LinkedBinaryTree;
import trees.Position;
import trees.Tree;

public class Exercise2 {
    public static void main(String[] args) {
        System.out.println("              A1              ");
        System.out.println("      B2              H2      ");
        System.out.println("  C3      F3      I3      J3  ");
        System.out.println("D4  E4  G4                    ");
        System.out.println();
        LinkedBinaryTree<String> tree = new LinkedBinaryTree<>();
        Position<String> root = tree.addRoot("A1");

        Position<String> b2 = tree.addLeft(root, "B2");
        Position<String> h2 = tree.addRight(root, "H2");

        Position<String> c3 = tree.addLeft(b2, "C3");
        Position<String> f3 = tree.addRight(b2, "F3");
        Position<String> i3 = tree.addLeft(h2, "I3");
        Position<String> j3 = tree.addRight(h2, "J3");

        Position<String> d4 = tree.addLeft(c3, "D4");
        Position<String> e4 = tree.addRight(c3, "E4");
        Position<String> g4 = tree.addLeft(f3, "G4");

        System.out.print("Subtree heights:\n");
        printTreeHeights(tree);
        System.out.println();
    }

    public static <E> void printTreeHeights(Tree<E> tree) {
        Position<E> root = tree.root();
        if (root != null)
            printTreeHeights(tree, root, 0);
    }

    private static <E> int printTreeHeights(Tree<E> tree, Position<E> current, int depth) {
        int maxChildHeight = -1;
        for (Position<E> child : tree.children(current)) {
            int childHeight = printTreeHeights(tree, child, depth + 1);
            maxChildHeight = Math.max(maxChildHeight, childHeight);
        }

        int currentHeight = maxChildHeight + 1;

        System.out.printf(
                "%s%s%s (height: %d, depth: %d)\n",
                " ".repeat(depth * 2),
                current.getElement(),
                " ".repeat(currentHeight * 2),
                currentHeight,
                depth);

        return currentHeight;
    }
}
