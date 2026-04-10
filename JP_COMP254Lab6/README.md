# JP_COMP254Lab6

> [!NOTE]
>
> The project structure has been changed to use the package path,
> `xyz.thegamecracks.comp254.lab6`.
> Exercise classes are contained in this package.

```java
$ gradlew run
Reusing configuration cache.

> Task :app:run
===== Exercise 1 =====
Benchmarking ChainHashMap with load factor 0.1...
  Completed in 476ms
Benchmarking ChainHashMap with load factor 0.2...
  Completed in 413ms
Benchmarking ChainHashMap with load factor 0.3...
  Completed in 487ms
Benchmarking ChainHashMap with load factor 0.4...
  Completed in 548ms
Benchmarking ChainHashMap with load factor 0.5...
  Completed in 631ms
Benchmarking ChainHashMap with load factor 0.6...
  Completed in 529ms
Benchmarking ChainHashMap with load factor 0.7...
  Completed in 717ms
Benchmarking ChainHashMap with load factor 0.8...
  Completed in 388ms
Benchmarking ChainHashMap with load factor 0.9...
  Completed in 549ms

===== Exercise 2 =====
Does map contain 123? false
What is the value at 123? null

Added 'Hello world!' at key 123
Does map contain 123? true
What is the value at 123? Hello world!

Replaced 'Hello world!' with null
Does map contain 123? true
What is the value at 123? null

Removed 'null' at key 123
Does map contain 123? false
What is the value at 123? null

BUILD SUCCESSFUL in 5s
2 actionable tasks: 2 executed
Configuration cache entry reused.
```
