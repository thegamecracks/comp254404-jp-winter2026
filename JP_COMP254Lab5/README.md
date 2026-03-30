# JP_COMP254Lab5

```java
$ gradlew run
Reusing configuration cache.

> Task :app:run
===== Exercise 1 =====
              A1
      B2              H2
  C3      F3      I3      J3
D4  E4  G4

Preorder:
    A1 => B2 => C3 => D4 => E4 => F3 => G4 => H2 => I3 => J3

===== Exercise 2 =====
              A1
      B2              H2
  C3      F3      I3      J3
D4  E4  G4

Subtree heights:
      D4 => 0
      E4 => 0
    C3   => 1
      G4 => 0
    F3   => 1
  B2     => 2
    I3 => 0
    J3 => 0
  H2   => 1
A1       => 3


===== Exercise 3 =====
{A: A1, B: B2, G: G4, D: D4, C: C3, I: I3, J: J3, E: E4, H: H2, F: F3}
A => A1
B => B2
C => C3
D => D4
E => E4
F => F3
G => G4
H => H2
I => I3
J => J3

BUILD SUCCESSFUL in 950ms
2 actionable tasks: 1 executed, 1 up-to-date
Configuration cache entry reused.
```
