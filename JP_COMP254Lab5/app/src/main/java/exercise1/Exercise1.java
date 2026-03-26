package exercise1;

import trees.BinaryTree;
import trees.LinkedBinaryTree;
import trees.Position;

public class Exercise1 {
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

        System.out.print("Preorder:\n    ");
        printPreorder(tree);
        System.out.println();
    }

    public static void printPreorder(LinkedBinaryTree<String> tree) {
        Position<String> current = tree.root();
        while (current != null) {
            System.out.print(current.getElement());
            current = preorderNext(tree, current);

            if (current != null)
                System.out.print(" => ");
        }
    }

    /**
     * Return the next node in pre-order traversal.
     *
     * Worse-case running time is O(n).
     */
    public static <E> Position<E> preorderNext(BinaryTree<E> tree, Position<E> p) {
        // If this is an internal node, continue traversing down.
        if (tree.left(p) != null)
            return tree.left(p);
        if (tree.right(p) != null)
            return tree.right(p);

        // We've reached an external node, go back up to the next available branch.
        Position<E> current = p;
        Position<E> parent = tree.parent(current);
        while (parent != null) {
            if (current == tree.left(parent) && tree.right(parent) != null) {
                return tree.right(parent);
            }

            current = parent;
            parent = tree.parent(parent);
        }

        return null;
    }
}
