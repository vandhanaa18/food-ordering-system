# Overview

This project is a Multi-Agent Food Ordering System designed to simulate the complete food ordering workflow using specialized AI agents. The system separates responsibilities across multiple agents.

# Current Architecture

The system consists of four primary agents:

## 1. Restaurant Recommendation Agent

- Understanding user food preferences
- Providing restaurant recommendations
- Supporting location-based restaurant discovery
- Generating natural language responses using an LLM

works completed:

- Improved recommendation quality
- Added support for location-aware restaurant suggestions
- Enabled LLM-generated recommendation responses

Tools Used:

- Google Gemini API (LLM)
- Python

## 2. Order Management Agent

- Managing customer orders
- Tracking ordered items
- Maintaining order history
- Displaying menu and pricing information

works completed:

- Improved order tracking workflow
- Added menu and pricing support
- Added order history functionality


Tools Used:

- Python
- In-memory data structures (lists and dictionaries)


## 3. Payment Verification Agent

- Simulating payment processing
- Verifying payment status

works completed:

- Generated payment IDs
- Added payment statuses
- Added timestamps for payment records

Tools Used:

- Python
- datetime module

## 4. Delivery Tracking Agent

- Tracking delivery progress
- Updating order status

works completed:

- Added delivery stages
- Added estimated delivery time (ETA)
- Added delivery partner information

Tools Used:

- Python
- In-memory data structures

Data Management

The system currently supports in-memory data storage.

Contributors:

1. Vandhanaa JV
2. Maharishi M
3. Safiya B
