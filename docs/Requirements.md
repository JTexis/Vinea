# Vinea - Software Requirements Specification (SRS)

Version (0.1 MVP)

Author: Roberto Texis

Status: Draft

Vinea is a cybersecurity SaaS platform that allows users to submit their website URLs for automated
 security assessments. The platform scans for common web security issues and generates
 an easy-to-understand report with identified
 vulnerabilities, risk levels, and recommendations for remediation.

2. Goals

The MVP aims to 
- Perform automated security assessments 
- Present results in a user-friendly dashboard
- Generate downloadable security reports
- Track scan history over time
- Help users improve their website security posture

3. Target Users

Small businesses
business owners who don't have security knowledge

Freelance developers 
Developers who want to cerify client websites

Agencies
Web agencies managing multiple customer websites

Security students
Students learning web security concepts

4. Functional Requirements 

4.1 Authentication 
users must be able to:
- Register
- Login
- Logout
- Reset Password
- Verify email
- Update profile

4.2 Dashboard 
Users can:
- View all websites
- View previous scans
- View scan status
- View security score

4.3 Website Management
Users can:
- Add website
- Remove website
- Rename website
- View website details

4.4 Scanner
Users can start a security scan 
The system should:

- Validate URL
- Queue the scan
- Execute checks
- Save results 
- Generate report

4.5 Reports 
Each report includes 
- Overall security score
- Findings
- Severity
- Description
- Recommendation
- Timestamp

5. Security Checks (MVP)
HTTPS
- HTTPS enabled
- Validate certificate
- Certificate expiration
HTTP Headers 
- CSP
- HSTS
- X-Frame-Options
- X-Content-Type-Options
- Referrer-Policy
- Permissions-Policy
Cookies
- Secure
- HTTP only
- SameSite
Server Information
- Server header
- Technology disclosure
- Framework disclosure
Configuration 
- Robots.txt
- Sitemap.xml
- Directory listing
- HTTPS redirect

6. Security Levels
- Critical
- High
- Medium
- Low
- Informational

7. Non-Functional Requirements
Performance
- Scan should begin with 10 seconds
Availability
- 99% uptime target
Security
- Password hashing
- JWT authentication
- HTTPS only
- CSRF protection where applicable
- Rate limiting
- Audit logs
Scalability
- Multiple scans running simultaneously

8. User Flow
- Register - Login - Dashboard - Add website - Start Scan - Scanning - Results - Download Report

9. Future Features
- Schedule scans
- Email alerts 
- Weekly reports
- Multple team members
- API access
- Browser extension
- Continuous monitoring
- Custom policies
- OWASP top 10 coverage
- AI -generated remediation suggestion  

10. Succes Metrics
- Average scan duration
- Number of scans 
- Returning Users 
- Websites protected
- Average security score improvement 

