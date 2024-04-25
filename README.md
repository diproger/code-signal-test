# Transactions and Wallets Test Project
## Features

- **Transactions API**: Allows CRUD operations for managing transactions.
- **Wallets API**: Allows CRUD operations for managing wallets.
- **Pagination**: Supports paginated responses for large datasets.
- **Sorting**: Allows sorting of transaction and wallet data based on specified fields.
- **Filtering**: Supports filtering of transaction and wallet data based on specified criteria.
- **Environment Configuration**: Uses a `.env` file for managing environment variables.
- **Execution Time Limit**: Enforces a 4-second execution time limit for API requests.
- **Memory Limit**: Enforces a 1 GB memory limit for API requests.

## Tech Stack

- **Python**: Version 3.10
- **Django**: Web framework for building the backend.
- **Django Rest Framework (DRF)**: Toolkit for building Web APIs.
- **MySql**: Database management system.
- **psutil**: Python library for system monitoring (used for memory limit enforcement).
