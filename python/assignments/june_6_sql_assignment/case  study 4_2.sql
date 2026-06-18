SELECT COUNT(DISTINCT node_id) AS unique_nodes
FROM customer_nodes;

SELECT 
    region_id,
    COUNT(DISTINCT node_id) AS node_count
FROM customer_nodes
GROUP BY region_id
ORDER BY region_id;

SELECT 
    region_id,
    COUNT(DISTINCT customer_id) AS customer_count
FROM customer_nodes
GROUP BY region_id
ORDER BY region_id;

SELECT 
    ROUND(AVG(DATEDIFF(end_date, start_date)), 2) AS avg_reallocation_days
FROM customer_nodes
WHERE end_date IS NOT NULL;

SELECT DISTINCT
    region_id,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY DATEDIFF(end_date, start_date)) 
        OVER (PARTITION BY region_id) AS median_days,
        
    PERCENTILE_CONT(0.8) WITHIN GROUP (ORDER BY DATEDIFF(end_date, start_date)) 
        OVER (PARTITION BY region_id) AS p80_days,
        
    PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY DATEDIFF(end_date, start_date)) 
        OVER (PARTITION BY region_id) AS p95_days
FROM customer_nodes
WHERE end_date IS NOT NULL;




SELECT 
    txn_type,
    COUNT(*) AS transaction_count,
    SUM(txn_amount) AS total_amount
FROM customer_transactions
GROUP BY txn_type;

SELECT 
    AVG(deposit_count) AS avg_deposit_count,
    AVG(total_amount) AS avg_deposit_amount
FROM (
    SELECT 
        customer_id,
        COUNT(*) AS deposit_count,
        SUM(txn_amount) AS total_amount
    FROM customer_transactions
    WHERE txn_type = 'deposit'
    GROUP BY customer_id
) t;

SELECT 
    month,
    COUNT(DISTINCT customer_id) AS customer_count
FROM (
    SELECT 
        customer_id,
        EXTRACT(MONTH FROM txn_date) AS month,
        SUM(CASE WHEN txn_type = 'deposit' THEN 1 ELSE 0 END) AS deposit_count,
        SUM(CASE WHEN txn_type = 'purchase' THEN 1 ELSE 0 END) AS purchase_count,
        SUM(CASE WHEN txn_type = 'withdrawal' THEN 1 ELSE 0 END) AS withdrawal_count
    FROM customer_transactions
    GROUP BY customer_id, EXTRACT(MONTH FROM txn_date)
) t
WHERE 
    deposit_count > 1 
    AND (purchase_count >= 1 OR withdrawal_count >= 1)
GROUP BY month
ORDER BY month;