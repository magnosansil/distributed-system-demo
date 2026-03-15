# Continuous Consistency Based on Number of Updates

## Overview

This project demonstrates the concept of **continuous consistency based
on the number of updates** in a distributed system.

In distributed systems, **data replication** is commonly used to improve
performance, reliability, and availability. However, maintaining
**consistency between replicas** is a significant challenge.

This project simulates a scenario where:

-   A **main server** stores the most recent version of a file
    containing stock market prices.
-   A **replica server** stores a replicated version of the same file.
-   The replica is **not updated immediately** after each modification.
-   Instead, the replica is synchronized only **after a fixed number of
    updates (X)**.

This creates a period where the replica may contain **outdated data**,
illustrating the concept of **continuous consistency**.

------------------------------------------------------------------------

## Architecture

The system follows a simple **client-server architecture** using **TCP
sockets**.

Components:

-   **Client**
-   **Main Server**
-   **Replica Server**

Communication flow:

    Client
       | \
       |  \
       |   \
       v    v
    Main Server     Replica Server

-   The **main server** maintains the most recent data.
-   The **replica server** maintains a delayed copy.
-   The **client** can request the file from either server.

------------------------------------------------------------------------

## Project Structure

    distributed-system-demo/

    client.py
    server_main.py
    server_replica.py

    stocks_server.txt
    stocks_replica.txt

    README.md

------------------------------------------------------------------------

## How It Works

1.  The **main server** stores the most recent stock prices.
2.  Each time the server performs an update, a counter is incremented.
3.  When the number of updates reaches a predefined threshold (**X =
    3**):

-   The server **synchronizes the replica**
-   The update counter resets

This means that during the first two updates, the **replica remains
outdated**, demonstrating **temporary inconsistency**.

------------------------------------------------------------------------

## Example Scenario

Initial state:

    Main Server
    PETR4 38.20
    VALE3 66.10
    ITUB4 31.50

    Replica
    PETR4 38.20
    VALE3 66.10
    ITUB4 31.50

After two updates:

    Main Server
    PETR4 40.20
    VALE3 68.10
    ITUB4 33.50

    Replica
    PETR4 38.20
    VALE3 66.10
    ITUB4 31.50

The replica is **temporarily inconsistent**.

After the third update:

    Main Server
    PETR4 41.20
    VALE3 69.10
    ITUB4 34.50

    Replica
    PETR4 41.20
    VALE3 69.10
    ITUB4 34.50

The replica is **synchronized again**.

------------------------------------------------------------------------

## Requirements

-   Python 3.x
-   No external libraries required

------------------------------------------------------------------------

## Running the System

Open **three terminals**.

### Start the main server

``` bash
python server_main.py
```

### Start the replica server

``` bash
python server_replica.py
```

### Start the client

``` bash
python client.py
```

------------------------------------------------------------------------

## Client Menu

The client provides the following options:

    1 - Download file from main server
    2 - Download file from replica
    3 - Update stock prices
    4 - Exit

This allows the user to observe:

-   **Consistent data**
-   **Outdated replica data**
-   **Replica synchronization after X updates**

------------------------------------------------------------------------

## Deployment Options

The system can be executed in two ways:

### Single Machine (Recommended for testing)

All components run on **localhost** using different ports:

-   Main Server → Port **5000**
-   Replica Server → Port **6000**

### Multiple Machines (Lab demonstration)

Each component can run on a different machine by replacing `localhost`
with the appropriate **IP address**.

------------------------------------------------------------------------

## Concepts Demonstrated

This project demonstrates the following distributed systems concepts:

-   Client-server architecture
-   Message exchange using sockets
-   Data replication
-   Temporary inconsistency between replicas
-   Continuous consistency based on update thresholds

------------------------------------------------------------------------

## Educational Purpose

This implementation was developed as part of a **Distributed Systems
course assignment**, demonstrating practical aspects of **data
replication and consistency models**.
