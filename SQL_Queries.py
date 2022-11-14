from datetime import datetime

A = """
SELECT avg(t2."avgMonth") as "avg"
FROM
    (SELECT
        t1."user",
        avg(t1."totalMonth") as "avgMonth"
    FROM
        (SELECT
            date_trunc('month', purchases."date") as "date",
            sum(items."price") as "totalMonth",
            users."userId" as "user"
        FROM "Purchases" as purchases
        INNER JOIN "Items" as items
        ON items."itemId" = purchases."itemId"
        INNER JOIN "Users" as users
        ON users."userId" = purchases."userId"
        WHERE users."age" >= {age_start} and users."age" <= {age_finish}
        GROUP BY "date", "user") as t1
    GROUP BY t1."user") as t2
"""
A1 = A.format(age_start=18, age_finish=25)
A2 = A.format(age_start=26, age_finish=35)

B = """
SELECT
    to_char(date_trunc('month', purchases."date"), 'MON') as "month",
    sum(items."price") as "totalMonth"
FROM "Purchases" as purchases
INNER JOIN "Items" as items
ON items."itemId" = purchases."itemId"
INNER JOIN "Users" as users
ON users."userId" = purchases."userId"
WHERE users."age" >= 35
GROUP BY "month"
ORDER BY "totalMonth" DESC 
LIMIT 1
"""

C = f"""
SELECT
    items."itemId" as "item"
FROM "Purchases" as purchases
INNER JOIN "Items" as items
ON items."itemId" = purchases."itemId"
WHERE to_char(date_trunc('year', purchases."date"), 'YYYY') = '{datetime.now().year}'
GROUP BY "item", to_char(date_trunc('year', purchases."date"), 'YYYY')
ORDER BY sum(items."price") DESC 
LIMIT 1
"""

D = """
SELECT
    t2."year",
    t2."item",
    max(t2."fraction") as "fraction"
FROM 
    (SELECT
        t1."year",
        t1."item",
        t1."fraction",
        dense_rank() OVER(PARTITION BY t1."year" ORDER BY "fraction" DESC) as "ratingInSection"
    FROM
        (SELECT
            items."itemId" as "item",
            to_char(date_trunc('year', purchases."date"), 'YYYY') as "year",
            sum(items."price"::decimal) OVER (PARTITION BY to_char(date_trunc('year', purchases."date"), 'YYYY'), items. "itemId") / 
                sum(items."price") OVER (PARTITION BY to_char(date_trunc('year', purchases."date"), 'YYYY')) as "fraction"

        FROM "Purchases" as purchases
        INNER JOIN "Items" as items
        ON items."itemId" = purchases."itemId") as t1
        ) as t2
WHERE t2."ratingInSection" <= 3
GROUP BY t2."year", t2."item"
ORDER BY t2."year" DESC, "fraction" DESC
"""



if __name__ == "__main__":
    print(datetime.now().year)