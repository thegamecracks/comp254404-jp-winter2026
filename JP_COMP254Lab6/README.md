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
Benchmarking ChainHashMap with load factor 0.1... (10/10)
  Completed 10 runs in 2,412ms
  Fastest run: 197ms
Benchmarking ChainHashMap with load factor 0.2... (10/10)
  Completed 10 runs in 2,302ms
  Fastest run: 179ms
Benchmarking ChainHashMap with load factor 0.3... (10/10)
  Completed 10 runs in 2,727ms
  Fastest run: 227ms
Benchmarking ChainHashMap with load factor 0.4... (10/10)
  Completed 10 runs in 1,947ms
  Fastest run: 146ms
Benchmarking ChainHashMap with load factor 0.5... (10/10)
  Completed 10 runs in 2,279ms
  Fastest run: 182ms
Benchmarking ChainHashMap with load factor 0.6... (10/10)
  Completed 10 runs in 2,666ms
  Fastest run: 219ms
Benchmarking ChainHashMap with load factor 0.7... (10/10)
  Completed 10 runs in 2,898ms
  Fastest run: 242ms
Benchmarking ChainHashMap with load factor 0.8... (10/10)
  Completed 10 runs in 1,892ms
  Fastest run: 134ms
Benchmarking ChainHashMap with load factor 0.9... (10/10)
  Completed 10 runs in 2,085ms
  Fastest run: 155ms

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

BUILD SUCCESSFUL in 22s
2 actionable tasks: 1 executed, 1 up-to-date
Configuration cache entry reused.
```
