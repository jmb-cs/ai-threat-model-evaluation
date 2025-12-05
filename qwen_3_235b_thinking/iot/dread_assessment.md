| Threat Type | Scenario | Damage Potential | Reproducibility | Exploitability | Affected Users | Discoverability | Risk Score |
|------------|----------|------------------|-----------------|----------------|----------------|-----------------|------------|
| Spoofing | An attacker spoofs the identity of the USB Video Camera to send malicious video frames to M3, which then get processed by downstream modules as legitimate input | 8 | 7 | 6 | 8 | 5 | 6.80 |
| Spoofing | An attacker spoofs the identity of M1 to intercept browser requests on the local LAN, conducting a man-in-the-middle attack against legitimate user sessions | 9 | 8 | 7 | 7 | 6 | 7.40 |
| Spoofing | An attacker spoofs Azure Cognitive Services endpoint to intercept OCR and Text-to-Speech requests from M3 | 9 | 7 | 6 | 9 | 7 | 7.60 |
| Tampering | An attacker intercepts and modifies WebSocket communications between M1, M2, and M3 on the local network | 9 | 8 | 7 | 8 | 6 | 7.60 |
| Tampering | An attacker tampers with telemetry data being sent from EdgeMetricsCollector to Application Insights by injecting falsified data | 7 | 7 | 6 | 7 | 8 | 7.00 |
| Tampering | An attacker tampers with video frames stored in Azure Storage that were uploaded by M2 for debugging purposes | 6 | 7 | 5 | 6 | 9 | 6.60 |
| Repudiation | A malicious insider alters or deletes telemetry data sent to Application Insights after performing unauthorized actions on the system | 9 | 6 | 5 | 8 | 4 | 6.40 |
| Repudiation | An attacker who gained access to M1 performs unauthorized operations via browser interface but the system lacks sufficient transaction logging | 9 | 8 | 7 | 8 | 6 | 7.60 |
| Repudiation | An external attacker tampers with logs sent to Azure Monitor by modifying timestamps or content during transmission | 8 | 7 | 6 | 8 | 7 | 7.20 |
| Information Disclosure | Connection strings for Azure services are exposed through insecure GitHub secrets management or CI/CD pipeline artifacts | 10 | 8 | 7 | 10 | 6 | 8.20 |
| Information Disclosure | Debugging video frames uploaded to Azure Storage contain personally identifiable information from camera feeds | 7 | 7 | 5 | 9 | 8 | 7.20 |
| Information Disclosure | WebSocket communications between M1, M2, and M3 lack encryption on the local network | 7 | 9 | 8 | 8 | 7 | 7.80 |
| Denial of Service | An attacker floods M1's HTTP endpoint with excessive requests from the browser interface | 7 | 9 | 8 | 8 | 6 | 7.60 |
| Denial of Service | An attacker sends specially crafted video frames via the USB Camera interface that cause resource exhaustion in M3 processing | 8 | 6 | 5 | 8 | 7 | 6.80 |
| Denial of Service | An attacker floods Azure Cognitive Services with excessive requests through M3 by manipulating the edge device | 8 | 7 | 6 | 9 | 6 | 7.20 |
| Elevation of Privilege | An attacker exploits vulnerabilities in M1 to gain shell access to the IoT Edge device and then escalate privileges to control EdgeRuntime | 10 | 7 | 6 | 9 | 5 | 7.40 |
| Elevation of Privilege | A compromised IoT Edge module accesses connection strings from memory and uses them to gain administrative access to Azure services | 10 | 7 | 6 | 10 | 7 | 8.00 |
| Elevation of Privilege | An attacker gains access to GitHub secrets containing Azure connection strings through a supply chain attack on CI/CD pipelines | 10 | 6 | 5 | 10 | 6 | 7.40 |