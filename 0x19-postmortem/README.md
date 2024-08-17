PORTMORTEM ISSUED ENCOUNTERED DURING WEBSTACK DEBUGGING #1
Duration:
Start: 2024-08-15, 19:45 WAT
End: 2024-08-15, 23:30 WAT
Total Duration: 3 hours 45 minutes
Impact:
All automated checkers for the project were failing, preventing the completion of further tasks. Approximately 100% of project-related tasks were blocked, affecting the ability to make progress on other critical deliverables.
Root Cause:
Nginx was not properly installed on both web servers, causing the service to fail to start. This led to a failure in establishing a connection to port 80, which resulted in the checkers being unable to access the web application for validation.
Timeline
19:45 WAT: Issue detected when the automated checkers began failing, and the web application was inaccessible.
19:50 WAT: Initial troubleshooting began by checking the server status and connectivity.
20:00 WAT: Attempted to restart Nginx on both servers but discovered that it was not installed correctly.
20:10 WAT: Checked logs and verified that Nginx was not running due to a failed installation.
20:20 WAT: Misleading path: Assumed the issue was related to firewall or network settings, leading to unnecessary checks.
21:00 WAT: Incident escalated to the DevOps team after confirming the issue was not network-related.
21:30 WAT: DevOps team identified the root cause and re-installed Nginx on both servers.
23:00 WAT: Nginx installation and configuration were completed, and the checkers began functioning correctly.
23:30 WAT: All services were restored, allowing tasks to resume.
Root Cause and Resolution
Root Cause:
The root cause of the outage was an incomplete Nginx installation on both web servers. The improperly installed Nginx service prevented it from starting, leading to an inability to establish a connection to port 80. This directly impacted the automated checkers, which rely on the web application being accessible.
Resolution:
The DevOps team re-installed Nginx on both web servers, ensuring that it was correctly configured and started. Once Nginx was operational, the connection to port 80 was restored, and the checkers were able to validate the tasks successfully.
Corrective and Preventative Measures
Improvements Needed:
Implement more robust deployment scripts to verify proper installation and configuration of critical services like Nginx.
Enhance monitoring to detect service failures before they impact automated processes like checkers.
Improve incident response procedures to avoid unnecessary troubleshooting steps.
TODO List:
Revise deployment scripts: Ensure Nginx installation is thoroughly tested in deployment scripts.
Add monitoring for Nginx service and port 80: Set up alerts for service downtime or port issues.
Create a post-deployment checklist: Ensure all critical services are running before project checkers are executed.
Conduct training sessions: Train the team on how to quickly diagnose and resolve issues related to service installations and configurations.
These actions aim to prevent similar disruptions in the future and enable more efficient handling of related issues.
