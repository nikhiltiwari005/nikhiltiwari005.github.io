---
title: "Demystifying == and .equals() in Java"
date: 2025-05-07 14:39:45 +0000
categories: ["Java World!"]
tags: []
---

### Demystifying == and .equals() in Java

*Understanding Reference Equality, Value Equality, hashCode(), Lombok, and Records*

![image](/assets/img/demystifying-and-equals-in-java/1_9uwOm7APqOPg7_B2hRlHEw.png)

In Java, comparing objects is not as straightforward as it seems. Developers often confuse == and .equals(), and overlook the role of hashCode(), which leads to subtle bugs — especially in collections like HashMap. In this post, we’ll dissect these concepts and explore modern alternatives like Lombok and Records.

### 🔍 == Operator — Reference Equality

The == operator checks whether**two object references point to the exact same memory location**.

```
Example example1 = new Example();Example example2 = new Example();example1 == example1; // trueexample1 == example2; // false
```

Even if example1 and example2 hold the**same values**, == returns false because they are different objects in memory.

### 🔍 .equals() Method — Value Equality (When Overridden)

By default, the .equals() method in Java is inherited from Object, and its behavior is identical to == — it checks**reference equality**.

```
public class Example {    public int id;}Example e1 = new Example(); e1.id = 1;Example e2 = new Example(); e2.id = 1;System.out.println(e1.equals(e2)); // false
```

But this can (and should) be overridden to compare**object contents**instead of memory references:

```
public class Example {    public int id;    @Override    public boolean equals(Object o) {        if (this == o) return true;        if (!(o instanceof Example)) return false;        Example other = (Example) o;        return this.id == other.id;    }    @Override    public int hashCode() {        return Objects.hash(id);    }}
```

Now:

```
Example e1 = new Example(); e1.id = 1;Example e2 = new Example(); e2.id = 1;System.out.println(e1.equals(e2)); // true
```

### ⚠️ == vs .equals() — What’s the Difference?

- == compares**object references**(memory location).
- .equals() compares**object references**by default.
- When overridden, .equals() can compare**object content**(values).
- Only .equals() can be overridden — == cannot.
- Java collections like HashMap use .equals() and hashCode() to function properly.

### 🤔 Why Do We Need hashCode()?

Whenever you override .equals(), you**must**also override hashCode().

Why?

Because hash-based collections (HashMap, HashSet, etc.) use:

1. hashCode() to find the**bucket**.
2. .equals() to find the**exact object**inside that bucket.

If two objects are equal by .equals(), they must have the**same hash code**— that’s the contract.

### Example Without hashCode Override:

```
Example e1 = new Example(); e1.id = 1;Example e2 = new Example(); e2.id = 1;System.out.println(e1.equals(e2));     // trueSystem.out.println(e1.hashCode());     // 9869869System.out.println(e2.hashCode());     // 8768872
```

Even though equals() returns true, the hashCode() values are different. If you store e1 in a HashMap and then look up e2, it won’t be found. Bug alert!

### ✅ Correct hashCode Implementation

```
@Overridepublic int hashCode() {    return Objects.hash(id);}
```

This ensures that logically equal objects return the same hash and behave correctly in collections.

### 💥 What If You Mutate a Key?

```
Map<Example, String> map = new HashMap<>();Example key = new Example(); key.id = 1;map.put(key, "value");// Mutate the keykey.id = 2;// This will failSystem.out.println(map.containsKey(key)); // false
```

**Mutating a field that affects .hashCode() breaks the map**. The object “moves” to a different bucket, but the map can’t find it anymore. This is why**keys in a hash-based map must be immutable**.

### 🛠️ Use Lombok to Avoid Boilerplate

Writing equals() and hashCode() manually is tedious and error-prone.

**Lombok**provides annotations to generate them automatically:

```
import lombok.EqualsAndHashCode;@EqualsAndHashCodepublic class Example {    public int id;}
```

Use @Data for a full package: getters, setters, toString, equals, and hashCode.

### 🚀 Use Records for Cleaner, Immutable Value Classes

Java introduced**records**in Java 14 (finalized in Java 16). Records are**immutable, concise, and perfect for DTOs and map keys**.

```
public record Example(int id) {}
```

This one-liner gives you:

- Constructor
- Getters
- equals()
- hashCode()
- toString()
- Immutable fields

No Lombok, no boilerplate — modern Java at its best.

### ✅ Summary — When to Use What?

- Use == when you care about**object identity**(i.e., same memory address).
- Use .equals() when comparing**values**— but remember to override it.
- Override hashCode() whenever you override .equals().
- Never use**mutable objects as map keys**.
- Use**Lombok**(@EqualsAndHashCode or @Data) to reduce boilerplate.
- Prefer**records**for clean, immutable value classes when possible.

