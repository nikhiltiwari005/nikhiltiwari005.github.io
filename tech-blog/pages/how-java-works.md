---
layout: post
title: "How Java Works Under the Hood"
description: "A deep dive into the JVM, bytecode, and what actually happens when you run a Java program."
date: 2026-05-27
author: Nikhil Tiwari
tag: Java
read_time: 6
---

Java is one of those languages that promises "write once, run anywhere" — but how does that actually work? Let's pull back the curtain.

## The Compilation Step

When you write Java code and run `javac MyClass.java`, the compiler doesn't produce machine code. It produces **bytecode** — a `.class` file that no hardware natively understands.

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

Run `javac Hello.java` and you get `Hello.class`. Try opening it — it's binary, not readable. That's bytecode.

## The JVM: The Real Hero

The **Java Virtual Machine (JVM)** is what actually runs your program. It reads the bytecode and executes it. Every OS has its own JVM implementation — that's what makes the "run anywhere" promise work.

The JVM does three big things:

1. **Class Loading** — finds and loads `.class` files into memory
2. **Bytecode Verification** — checks that the bytecode is safe and valid
3. **Execution** — runs the bytecode, either interpreted or compiled

## Interpreted vs. JIT Compiled

Early JVMs were purely **interpreted** — they read bytecode one instruction at a time and executed it. Slow, but simple.

Modern JVMs use **JIT (Just-In-Time) compilation**. The JVM watches which parts of your code run frequently (called "hot paths"), and compiles those to native machine code at runtime.

```
Your Code (.java)
     ↓ javac
  Bytecode (.class)
     ↓ JVM loads
  Interpreted (initially)
     ↓ hotspot detected
  Native Machine Code (JIT)
```

This is why Java "warms up" — the longer it runs, the faster it gets.

## The Heap and Stack

The JVM manages memory in two main areas:

| Area | What lives here |
|------|----------------|
| **Stack** | Method calls, local variables, references |
| **Heap** | All objects created with `new` |

Each thread gets its own stack. The heap is shared across all threads — which is why concurrency is tricky in Java.

## Garbage Collection

You never call `free()` in Java. The **Garbage Collector (GC)** automatically reclaims memory from objects that are no longer reachable.

The default GC in modern Java (17+) is **G1 (Garbage First)**, which divides the heap into regions and collects the ones with the most garbage first.

> **Tip:** GC pauses ("stop the world" events) are why latency-sensitive applications tune JVM flags carefully.

## Summary

When you run `java Hello`:

1. The JVM's **class loader** finds `Hello.class`
2. The **bytecode verifier** checks it's safe
3. The `main` method is called
4. **JIT** compiles hot paths to native code over time
5. The **GC** cleans up objects you no longer need

That's the magic behind the platform independence — one set of bytecode, many JVM implementations, every OS.
