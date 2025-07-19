# DhaScan - AI-Powered Web Vulnerability Scanner

```
██████╗ ██╗  ██╗ █████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██║  ██║██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
██║  ██║███████║███████║███████╗██║     ███████║██╔██╗ ██║
██║  ██║██╔══██║██╔══██║╚════██║██║     ██╔══██║██║╚██╗██║
██████╔╝██║  ██║██║  ██║███████║╚██████╗██║  ██║██║ ╚████║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
```

🌐 **DhaScan** - Created by **Ronit Paikray** ❤️  
**Slogan**: *Think Like an Attacker. Defend Like a Pro.*

DhaScan is a robust, AI-powered web vulnerability scanner designed for security researchers, penetration testers, and developers to identify and mitigate security weaknesses in modern web applications. With over 227 vulnerability tests, advanced technology fingerprinting, and a multi-threaded scanning engine, DhaScan provides comprehensive security assessments with detailed reports to facilitate remediation. Built with extensibility and usability in mind, it combines AI-driven detection with a user-friendly CLI interface.

## Project Overview

DhaScan is a Python-based tool that performs automated security testing for web applications. It leverages an AI vulnerability engine to detect a wide range of vulnerabilities, from common issues like SQL Injection and XSS to advanced misconfigurations in Single Page Applications (SPAs). The tool is designed to mimic an attacker's approach while providing actionable insights for defenders. Key aspects include:

- **AI-Powered Detection**: Utilizes pattern matching, behavioral analysis, and (placeholder for future) machine learning models to identify vulnerabilities with high accuracy.
- **Comprehensive Testing**: Covers 227+ vulnerability types, including OWASP Top 10 and CWE-aligned issues.
- **Technology Fingerprinting**: Identifies web servers, CMS, frameworks, JavaScript libraries, and more to provide context for vulnerabilities.
- **Flexible Reporting**: Generates reports in JSON, HTML, or PDF formats for easy integration into workflows.
- **Ethical Design**: Built for authorized security testing with clear warnings about legal use.

## Features

DhaScan offers a rich set of features to support thorough security assessments:

1. **227+ Vulnerability Tests**:
   - Covers SQL Injection, Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF), Server-Side Request Forgery (SSRF), and more.
   - Tests for misconfigurations in SPAs, API endpoints, and security headers.
   - Aligns with OWASP Top 10 and CWE standards for industry relevance.

2. **AI Vulnerability Engine**:
   - Uses predefined patterns and behavioral profiles for accurate detection.
   - Reduces false positives through confirmation checks.
   - Extensible with custom vulnerability patterns.

3. **Technology Fingerprinting**:
   - Detects web servers (e.g., Apache, Nginx), CMS (e.g., WordPress, Drupal), frameworks (e.g., Django, Laravel), JavaScript libraries, and databases.
   - Identifies security headers (e.g., Content-Security-Policy, X-Frame-Options) to assess protection levels.

4. **Multi-Threaded Scanning**:
   - Supports configurable threading for optimized performance.
   - Concurrently tests multiple endpoints to reduce scan time.

5. **Flexible Output Formats**:
   - JSON for programmatic use.
   - HTML for readable, browser-friendly reports.
   - PDF for professional documentation.

6. **Proxy Support**:
   - Configurable proxy settings for scanning through intermediaries like Burp Suite.

7. **Extensibility**:
   - Modular design allows adding custom payloads and vulnerability patterns.
   - Supports YAML configuration for advanced users (requires `pyyaml`).

8. **User-Friendly CLI**:
   - Intuitive command-line interface with clear help documentation.
   - Customizable scan parameters (e.g., threads, output format).

## Requirements

- **Python**: 3.8 or higher (due to use of dataclasses and advanced typing)
- **Required Dependencies**:
  - `requests>=2.25.0` (for HTTP requests)
- **Optional Dependencies** (recommended for full functionality):
  - `beautifulsoup4>=4.9.0` (for enhanced HTML parsing of web pages)
  - `pyyaml>=5.4.0` (for YAML configuration support)

## Installation

Follow these steps to set up DhaScan on your system:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Ronit-paikray/DhaScan.git
   cd DhaScan
   ```

2. **Run the Setup Script**:
   The included `setup_dhascan.py` script automates dependency installation and setup.
   ```bash
   python3 setup_dhascan.py
   ```

   The setup script will:
   - Verify Python 3.8+ compatibility.
   - Install required (`requests`) and optional (`beautifulsoup4`, `pyyaml`) dependencies.
   - Generate a `requirements.txt` file.
   - Display usage instructions.

3. **Manual Installation** (alternative):
   Install dependencies using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

   Or install individually:
   ```bash
   pip install requests beautifulsoup4 pyyaml
   ```

## Usage

DhaScan is controlled via a command-line interface (CLI). The primary command structure is:

```bash
python3 DhaScan.py -u <target_url> [options]
```

### Command-Line Options
| Option | Description | Default |
|--------|-------------|---------|
| `-u, --url` | Target URL to scan (required) | None |
| `-o, --output` | Output file for the scan report | None |
| `--format` | Report format (`json`, `html`, `pdf`) | `json` |
| `--threads` | Number of scanning threads | 5 |

### Example Commands

1. **Basic Scan**:
   Scan a target URL and output results to the console:
   ```bash
   python3 DhaScan.py -u https://example.com
   ```

2. **Save Report in JSON**:
   Save the scan report to a JSON file:
   ```bash
   python3 DhaScan.py -u https://example.com --output report.json --format json
   ```

3. **Generate HTML Report with Custom Threads**:
   Create an HTML report with 10 threads for faster scanning:
   ```bash
   python3 DhaScan.py -u https://example.com --output report.html --format html --threads 10
   ```

4. **View Help**:
   Display all available options:
   ```bash
   python3 DhaScan.py --help
   ```

### Using Specific Features

1. **Vulnerability Scanning**:
   - DhaScan automatically runs all 227+ tests against the target URL.
   - Example: To test for SQL Injection and XSS:
     ```bash
     python3 DhaScan.py -u https://example.com
     ```
   - The AI engine will analyze responses for signs of vulnerabilities (e.g., SQL error messages, reflected XSS payloads).

2. **Technology Fingerprinting**:
   - Automatically performed during the scan.
   - Results are included in the report, detailing detected web servers, CMS, frameworks, etc.
   - Example output in JSON:
     ```json
     {
       "tech_stack": {
         "web_server": ["Apache/2.4.41"],
         "cms": ["WordPress"],
         "javascript_libs": ["jQuery 3.5.1"],
         "security_headers": {
           "Content-Security-Policy": false,
           "X-Frame-Options": true
         }
       }
     }
     ```

3. **Customizing Scan Threads**:
   - Use the `--threads` option to adjust concurrency based on your system's capabilities.
   - Example: For a high-performance system:
     ```bash
     python3 DhaScan.py -u https://example.com --threads 20
     ```

4. **Proxy Configuration**:
   - Configure a proxy (e.g., for Burp Suite) by modifying the `config` dictionary in `DhaScan.py`:
     ```python
     scanner = DhaScan({
         'threads': 5,
         'proxy': {
             'http': 'http://127.0.0.1:8080',
             'https': 'http://127.0.0.1:8080'
         }
     })
     ```

5. **Extending with Custom Patterns**:
   - Add custom vulnerability patterns to the `AIVulnEngine._load_vulnerability_patterns` method.
   - Example: To add a new SQL Injection pattern:
     ```python
     'sql_injection': [
         {'pattern': r'new_error_pattern', 'confidence': 80},
         # Existing patterns...
     ]
     ```
   - Requires `pyyaml` for loading patterns from YAML files (future feature).

6. **Report Generation**:
   - Use the `--format` option to select the output format.
   - Example for PDF output:
     ```bash
     python3 DhaScan.py -u https://example.com --output report.pdf --format pdf
     ```

## Sample Output
A typical scan produces output like this:

```
[+] Starting DhaScan vulnerability assessment
[+] Target: https://example.com
[+] Detected Technologies: Apache/2.4.41, WordPress
[+] Scanning for 227+ vulnerabilities...
[+] Scan completed in 15.67 seconds
[+] Found 3 confirmed vulnerabilities
[+] Report saved to: report.json
```

The JSON report might look like:
```json
{
  "target_url": "https://example.com",
  "vulnerabilities": [
    {
      "vuln_id": "SQLI-001",
      "name": "SQL Injection",
      "severity": "High",
      "affected_url": "https://example.com/login",
      "description": "Potential SQL Injection vulnerability detected",
      "remediation": "Use prepared statements and parameterized queries"
    },
    ...
  ],
  "tech_stack": {
    "web_server": ["Apache/2.4.41"],
    "cms": ["WordPress"],
    ...
  },
  "scan_duration": 15.67
}
```

## Notes
- **Optional Dependencies**: Install `beautifulsoup4` for advanced HTML parsing and `pyyaml` for YAML configuration support. Without these, some features (e.g., form parsing, custom config files) may be limited.
- **Ethical Use**: DhaScan is designed for authorized security testing. Always obtain explicit permission before scanning any system. Unauthorized scanning may be illegal.
- **Performance**: Adjust the `--threads` option based on your system's resources to optimize scan speed without overwhelming the target server.
- **False Positive Reduction**: The AI engine includes confirmation checks to minimize false positives, but manual verification is recommended.

## Contributing
We welcome contributions to enhance DhaScan! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

Please ensure your code follows PEP 8 style guidelines and includes appropriate tests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
Created by **Ronit Paikray**  
For questions, bug reports, or feedback, please open an issue on GitHub.

---
*Think Like an Attacker. Defend Like a Pro.*
