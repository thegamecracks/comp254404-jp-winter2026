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
  Completed 10 runs in 2,365ms
  Fastest run: 188ms
Benchmarking ChainHashMap with load factor 0.2... (10/10)
  Completed 10 runs in 2,403ms
  Fastest run: 177ms
Benchmarking ChainHashMap with load factor 0.3... (10/10)
  Completed 10 runs in 2,572ms
  Fastest run: 215ms
Benchmarking ChainHashMap with load factor 0.4... (10/10)
  Completed 10 runs in 2,392ms
  Fastest run: 176ms
Benchmarking ChainHashMap with load factor 0.5... (10/10)
  Completed 10 runs in 2,297ms
  Fastest run: 195ms
Benchmarking ChainHashMap with load factor 0.6... (10/10)
  Completed 10 runs in 2,396ms
  Fastest run: 197ms
Benchmarking ChainHashMap with load factor 0.7... (10/10)
  Completed 10 runs in 3,024ms
  Fastest run: 217ms
Benchmarking ChainHashMap with load factor 0.8... (10/10)
  Completed 10 runs in 1,799ms
  Fastest run: 148ms
Benchmarking ChainHashMap with load factor 0.9... (10/10)
  Completed 10 runs in 1,866ms
  Fastest run: 157ms
Fastest load factor: 0.8 (148ms)

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
2 actionable tasks: 2 executed
Configuration cache entry reused.
```
