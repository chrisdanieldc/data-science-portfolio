# SQL Query Examples

SQL reference covering basic to advanced patterns. Works on Snowflake, PostgreSQL, MySQL, and Oracle.

## What's Included

### Create Table (`create table.md`)
DDL example with CREATE TABLE statement and sample data inserts. Creates a global dataset with 20 rows spanning multiple regions (North America, EMEA, APAC, LATAM) and countries.

### Aggregate Functions (`Aggregate Functions.md`)
Standard aggregations (SUM, AVG, MIN, MAX, COUNT) plus window functions for cumulative calculations. Covers GROUP BY, HAVING clauses, and PARTITION BY for analytical queries.

Example: Running totals by region using `SUM() OVER (PARTITION BY region ORDER BY date)`

### Case Statements (`Case Statement.md`)
Conditional logic in SQL. Shows how to use CASE for IF-ELSE style transformations, data categorization, and lookup functions. Includes examples in both SELECT and WHERE clauses.

### Joins (`Joins.md`)
Multi-table join patterns with INNER JOIN. Demonstrates joining multiple tables and filtering on joined data.

### String Manipulation (`String Manupilation.md`)
Common string operations: concatenation (||), substring extraction (SUBSTR), text replacement (REPLACE), and length calculation (LENGTH).

### Date Functions (`Date functions.md`)
Working with dates and times: timezone conversion across regions, extracting date components (year, month, day, day of week), date formatting, and date arithmetic. Useful when your systems run on UTC but your business operates in different timezones.

### Nested Queries (`Nested Query.md`)
Complex multi-level subqueries (4+ levels deep). Includes window functions like DENSE_RANK with PARTITION BY, multiple joins, and aggregations within subqueries. Real example analyzing support ticket volumes by state and industry.

This is the most advanced file - shows production-level query patterns.

### Access Control (`Granting and revoking access.md`)
User permission management with GRANT and REVOKE. Covers role assignment (READER, OWNER, WRITER) and permission removal.

## Sample Data

All queries use a consistent sample dataset with global company data across multiple regions. The create table file has the full schema and 20 sample records.

## Skill Progression

**Basic**: Table creation, simple aggregations, basic joins

**Intermediate**: String/date functions, CASE statements, window functions

**Advanced**: Nested subqueries with multiple levels, complex window functions, multi-table analytical queries

## Usage

These are reference examples, not runnable scripts. Start with `create table.md` to set up your sample data, then browse the topic-specific files for patterns you can adapt to your own queries.

The nested query examples in particular show patterns you'd see in production analytics - things like ranking data within partitions, calculating running totals, and combining multiple data sources.
