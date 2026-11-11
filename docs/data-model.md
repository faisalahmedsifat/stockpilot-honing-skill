# Data Model Planning

Candidate domains:

- Identity: users, organizations, memberships, roles, refresh tokens
- Catalog: products, categories, units of measure
- Warehouse: warehouses, inventory balances, stock movements, reservations, transfers
- Procurement: suppliers, requisitions, requisition items, purchase orders, purchase order items
- Receiving: goods receipts, goods receipt items, discrepancies
- Sales: customers, sales orders, sales order items
- Fulfillment: pick lists, shipments, shipment items
- Governance: audit logs, approvals, idempotency records
- AI (later): documents, document chunks, assistant interactions

Define keys, constraints, tenant ownership, indexes, deletion behavior, and transaction boundaries before implementing migrations.
