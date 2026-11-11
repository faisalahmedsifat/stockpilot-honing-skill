# Product Brief: StockPilot

## Problem

Wholesale distributors often coordinate purchasing, warehouse stock, and customer orders across spreadsheets and disconnected systems. This creates inaccurate availability, avoidable stockouts, excess inventory, weak auditability, and delayed fulfillment.

## Target customer

Small and mid-sized wholesale distributors operating multiple warehouses and buying from multiple suppliers.

## Primary users

- Organization owner: business-wide visibility and configuration
- Operations manager: inventory, transfers, and fulfillment oversight
- Purchasing manager: suppliers, requisitions, purchase orders, approvals
- Warehouse operator: receiving, picking, packing, and stock counts
- Sales operator: customer orders and availability checks
- Viewer: read-only operational reporting

## Core workflow

1. A sales operator creates a customer order.
2. The system checks available-to-promise inventory.
3. Stock is reserved atomically for the order.
4. Insufficient stock can trigger a purchase requisition.
5. An authorized purchasing manager approves and issues a purchase order.
6. Warehouse staff record full or partial goods receipts and discrepancies.
7. Accepted quantities update the inventory ledger.
8. Warehouse staff pick and dispatch the customer order.
9. Managers review operational and supplier performance.

## MVP boundaries

- Multi-tenant organizations and role-based access
- Product and supplier catalog
- Multiple warehouses
- Inventory balances and immutable stock movement history
- Purchase requisitions, approvals, purchase orders, and goods receipts
- Customer orders and stock reservations
- Basic operational dashboard and audit trail

## Later capabilities

- Supplier integrations and notifications
- Background imports and scheduled reports
- Demand forecasting and replenishment suggestions
- Natural-language analytics grounded in tenant data
- Supplier-document retrieval using RAG

## Non-negotiable business invariants

- A reservation must never cause available stock to become negative.
- A stock change must have a traceable movement record and reason.
- A goods receipt must not exceed ordered quantity without an explicit exception workflow.
- Tenant data must never be accessible across organization boundaries.
- Approval permissions must be enforced server-side.
- Retried commands must not duplicate financial or inventory effects.
