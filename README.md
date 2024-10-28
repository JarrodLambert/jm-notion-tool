# Notion Toolkit

Welcome to the Notion Toolkit! This project is designed to help users interact with their Notion databases more efficiently. Currently, it includes functionality to copy entries from one Notion database to another, with options to map multi-select values. Future updates will expand this toolkit to include more features.

## Features

- Copy entries from a source Notion database to a target database.
- Map multi-select values from the source to different values in the target.
- Easily configure and manage sensitive information using environment variables.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/notion-toolkit.git
   cd notion-toolkit
   ```

2. **Set Up a Virtual Environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**

   Create a `.env` file in the root directory and add your Notion API token:

   ```plaintext
   NOTION_API_TOKEN=your_notion_api_token_here
   ```

5. **Run the Script**

   ```bash
   python main.py
   ```

## Usage

- **Copy Entries**: The script currently copies entries from a specified source database to a target database, with options to map multi-select values.
- **Mapping Multi-Select Values**: Customize the `multi_select_mapping` dictionary in `main.py` to map source values to target values.

## Future Development

- **Enhanced Mapping**: Add support for mapping other property types, such as select and date.
- **Batch Operations**: Implement batch processing for large datasets.
- **User Interface**: Develop a simple UI for easier configuration and execution.
- **Additional Integrations**: Explore integrations with other tools and services.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any features or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, please open an issue or contact me at [jarrod@juniormajor.com](mailto:jarrod@juniormajor.com).
