from app import app, db, User, Question, SecurityTopic
from werkzeug.security import generate_password_hash

def init_db():
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Create admin user
        admin = User(email='admin@cybersec.com', is_hr=True)
        admin.set_password('AdminPass123!')
        db.session.add(admin)

        # Create security topics with training content
        topics = [
            {
                'title': 'Password Security',
                'description': 'Learn best practices for creating and managing secure passwords',
                'content': """
                    <h3>Password Security Fundamentals</h3>
                    <p>Strong passwords are your first line of defense against unauthorized access to your accounts and personal information. Follow these essential guidelines to create and maintain secure passwords:</p>
                    
                    <h3>Password Creation Guidelines</h3>
                    <ul>
                        <li>Use at least 12 characters</li>
                        <li>Include uppercase and lowercase letters</li>
                        <li>Add numbers and special characters</li>
                        <li>Avoid personal information</li>
                        <li>Use unique passwords for each account</li>
                    </ul>

                    <h3>Password Management Tips</h3>
                    <ol>
                        <li>Use a password manager to store complex passwords</li>
                        <li>Enable two-factor authentication when available</li>
                        <li>Change passwords periodically</li>
                        <li>Never share passwords with others</li>
                        <li>Avoid storing passwords in plain text</li>
                    </ol>

                    <h3>Common Password Mistakes</h3>
                    <p>Avoid these common mistakes that can compromise your security:</p>
                    <ul>
                        <li>Using the same password everywhere</li>
                        <li>Writing passwords on sticky notes</li>
                        <li>Using obvious patterns (qwerty, 123456)</li>
                        <li>Including personal information</li>
                    </ul>
                """
            },
            {
                'title': 'Phishing Awareness',
                'description': 'Identify and protect yourself from phishing attempts',
                'content': """
                    <h3>Understanding Phishing Attacks</h3>
                    <p>Phishing is a cybercrime where attackers pose as legitimate institutions to steal sensitive information. Learn how to identify and protect yourself from these attacks.</p>

                    <h3>Common Phishing Indicators</h3>
                    <ul>
                        <li>Urgent or threatening language</li>
                        <li>Suspicious sender addresses</li>
                        <li>Generic greetings</li>
                        <li>Requests for sensitive information</li>
                        <li>Poor grammar or spelling</li>
                    </ul>

                    <h3>Protection Strategies</h3>
                    <ol>
                        <li>Never click suspicious links</li>
                        <li>Verify sender identities</li>
                        <li>Use spam filters</li>
                        <li>Keep software updated</li>
                        <li>Report suspicious emails</li>
                    </ol>

                    <h3>Real-World Examples</h3>
                    <p>Common phishing scenarios to watch for:</p>
                    <ul>
                        <li>Bank account verification requests</li>
                        <li>Prize winning notifications</li>
                        <li>Tech support scams</li>
                        <li>Social media friend requests</li>
                    </ul>
                """
            },
            {
                'title': 'Data Protection',
                'description': 'Learn how to protect sensitive data in the workplace',
                'content': """
                    <h3>Data Protection Basics</h3>
                    <p>Protecting sensitive data is crucial in today's digital workplace. Understanding proper data handling procedures helps prevent breaches and maintain compliance.</p>

                    <h3>Types of Sensitive Data</h3>
                    <ul>
                        <li>Personal Identifiable Information (PII)</li>
                        <li>Financial records</li>
                        <li>Healthcare information</li>
                        <li>Customer data</li>
                        <li>Proprietary information</li>
                    </ul>

                    <h3>Security Measures</h3>
                    <ol>
                        <li>Use encryption for sensitive files</li>
                        <li>Implement access controls</li>
                        <li>Regular data backups</li>
                        <li>Secure file sharing methods</li>
                        <li>Proper data disposal</li>
                    </ol>

                    <h3>Best Practices</h3>
                    <p>Follow these guidelines for data protection:</p>
                    <ul>
                        <li>Lock your computer when away</li>
                        <li>Use secure networks only</li>
                        <li>Avoid unauthorized software</li>
                        <li>Report security incidents</li>
                    </ul>
                """
            },
            {
                'title': 'Social Engineering',
                'description': 'Understanding and defending against social engineering attacks',
                'content': """
                    <h3>Understanding Social Engineering</h3>
                    <p>Social engineering is the art of manipulating people into giving up confidential information or performing actions that compromise security. These attacks exploit human psychology rather than technical vulnerabilities.</p>

                    <h3>Common Social Engineering Tactics</h3>
                    <ul>
                        <li>Pretexting (Creating a false scenario)</li>
                        <li>Baiting (Offering something enticing)</li>
                        <li>Quid Pro Quo (Offering a service in exchange for information)</li>
                        <li>Tailgating (Following someone into a restricted area)</li>
                        <li>Impersonation (Pretending to be someone else)</li>
                    </ul>

                    <h3>Red Flags to Watch For</h3>
                    <ol>
                        <li>Unsolicited contact from unknown individuals</li>
                        <li>Requests for sensitive information</li>
                        <li>Creating a sense of urgency</li>
                        <li>Offers that seem too good to be true</li>
                        <li>Appeals to vanity or fear</li>
                    </ol>

                    <h3>Protection Strategies</h3>
                    <ul>
                        <li>Verify identities through official channels</li>
                        <li>Never share sensitive information without verification</li>
                        <li>Be skeptical of unsolicited requests</li>
                        <li>Follow security protocols consistently</li>
                        <li>Report suspicious activities</li>
                    </ul>
                """
            },
            {
                'title': 'Mobile Device Security',
                'description': 'Protect your mobile devices from security threats',
                'content': """
                    <h3>Mobile Security Fundamentals</h3>
                    <p>Mobile devices often contain sensitive personal and corporate data. Proper security measures are essential to protect this information from unauthorized access and cyber threats.</p>

                    <h3>Essential Security Measures</h3>
                    <ul>
                        <li>Use strong device passwords/biometrics</li>
                        <li>Enable device encryption</li>
                        <li>Install security updates promptly</li>
                        <li>Use VPN on public networks</li>
                        <li>Enable remote wiping capability</li>
                    </ul>

                    <h3>App Security</h3>
                    <ol>
                        <li>Download apps only from official stores</li>
                        <li>Review app permissions carefully</li>
                        <li>Keep apps updated</li>
                        <li>Remove unused applications</li>
                        <li>Avoid jailbreaking/rooting devices</li>
                    </ol>

                    <h3>Data Protection Tips</h3>
                    <ul>
                        <li>Back up data regularly</li>
                        <li>Use secure cloud storage</li>
                        <li>Avoid storing sensitive data locally</li>
                        <li>Use secure communication apps</li>
                        <li>Enable auto-lock features</li>
                    </ul>
                """
            },
            {
                'title': 'Incident Response',
                'description': 'Learn how to respond to security incidents effectively',
                'content': """
                    <h3>Incident Response Basics</h3>
                    <p>Knowing how to respond to security incidents is crucial for minimizing damage and preventing future occurrences. A well-planned response can make the difference between a minor issue and a major breach.</p>

                    <h3>Incident Response Steps</h3>
                    <ol>
                        <li>Identification
                            <ul>
                                <li>Recognize security incidents</li>
                                <li>Document initial observations</li>
                                <li>Assess the severity</li>
                            </ul>
                        </li>
                        <li>Containment
                            <ul>
                                <li>Isolate affected systems</li>
                                <li>Change compromised credentials</li>
                                <li>Preserve evidence</li>
                            </ul>
                        </li>
                        <li>Eradication
                            <ul>
                                <li>Remove malware/threats</li>
                                <li>Fix vulnerabilities</li>
                                <li>Update security measures</li>
                            </ul>
                        </li>
                        <li>Recovery
                            <ul>
                                <li>Restore systems safely</li>
                                <li>Monitor for suspicious activity</li>
                                <li>Verify system integrity</li>
                            </ul>
                        </li>
                    </ol>

                    <h3>Best Practices</h3>
                    <ul>
                        <li>Report incidents immediately</li>
                        <li>Document all actions taken</li>
                        <li>Follow established procedures</li>
                        <li>Maintain communication with stakeholders</li>
                        <li>Learn from incidents to prevent recurrence</li>
                    </ul>
                """
            }
        ]

        # Add topics to database
        for topic_data in topics:
            topic = SecurityTopic(
                title=topic_data['title'],
                description=topic_data['description'],
                content=topic_data['content']
            )
            db.session.add(topic)
            db.session.flush()  # This assigns IDs to the topics

            # Add topic-specific questions
            if topic.title == 'Password Security':
                questions = [
                    {
                        'question': 'What is the minimum recommended password length?',
                        'correct': '12 characters',
                        'options': '8 characters,10 characters,12 characters,16 characters'
                    },
                    {
                        'question': 'Which of the following is a good password practice?',
                        'correct': 'Using unique passwords for each account',
                        'options': 'Using the same password everywhere,Using simple passwords,Using personal information,Using unique passwords for each account'
                    },
                    {
                        'question': 'What is the best way to store multiple complex passwords?',
                        'correct': 'Use a password manager',
                        'options': 'Write them in a notebook,Store them in a text file,Use a password manager,Save them in your browser'
                    },
                    {
                        'question': 'Which password would be considered the strongest?',
                        'correct': 'Tr@ff1c*L1ght$2025',
                        'options': 'Password123,MyBirthday1990,Tr@ff1c*L1ght$2025,CompanyName2025'
                    },
                    {
                        'question': 'How often should you change critical passwords?',
                        'correct': 'Every 3-6 months',
                        'options': 'Never,Once a year,Every 3-6 months,Only when compromised'
                    }
                ]
            elif topic.title == 'Phishing Awareness':
                questions = [
                    {
                        'question': 'Which is a common indicator of a phishing email?',
                        'correct': 'Urgent or threatening language',
                        'options': 'Company logo,Urgent or threatening language,Professional signature,Clear subject line'
                    },
                    {
                        'question': 'What should you do with suspicious emails?',
                        'correct': 'Report them to IT security',
                        'options': 'Forward them to colleagues,Click links to verify,Report them to IT security,Reply to verify sender'
                    },
                    {
                        'question': 'What is a sign of a suspicious email sender address?',
                        'correct': 'Slight misspelling of a legitimate domain',
                        'options': 'Contains the company name,Slight misspelling of a legitimate domain,Uses https,Has a signature'
                    },
                    {
                        'question': 'What should you do before clicking a link in an email?',
                        'correct': 'Hover over it to preview the URL',
                        'options': 'Click it quickly,Hover over it to preview the URL,Download it first,Copy and paste it'
                    },
                    {
                        'question': 'Which attachment type is most likely to be malicious?',
                        'correct': '.exe file',
                        'options': '.txt file,.pdf file,.exe file,.jpg file'
                    }
                ]
            elif topic.title == 'Data Protection':
                questions = [
                    {
                        'question': 'What is considered sensitive data?',
                        'correct': 'Personal Identifiable Information (PII)',
                        'options': 'Public records,Marketing materials,Personal Identifiable Information (PII),Company blog posts'
                    },
                    {
                        'question': 'What is a best practice for data protection?',
                        'correct': 'Encrypting sensitive files',
                        'options': 'Sharing passwords,Encrypting sensitive files,Using public WiFi,Storing data on personal devices'
                    },
                    {
                        'question': 'How should you dispose of sensitive documents?',
                        'correct': 'Shred them using a cross-cut shredder',
                        'options': 'Throw them in the trash,Recycle them,Shred them using a cross-cut shredder,Delete them from recycle bin'
                    },
                    {
                        'question': 'What is the best practice for backing up sensitive data?',
                        'correct': 'Regular encrypted backups to secure storage',
                        'options': 'Email to personal account,Regular encrypted backups to secure storage,Save to public cloud,Copy to USB drive'
                    },
                    {
                        'question': 'When sharing sensitive data, you should:',
                        'correct': 'Use encrypted channels and verify recipient',
                        'options': 'Send via regular email,Post in team chat,Use encrypted channels and verify recipient,Share via public link'
                    }
                ]
            elif topic.title == 'Social Engineering':
                questions = [
                    {
                        'question': 'What is social engineering?',
                        'correct': 'Manipulating people to give up confidential information',
                        'options': 'Writing malicious code,Manipulating people to give up confidential information,Breaking encryption,Installing antivirus software'
                    },
                    {
                        'question': 'Which is a common social engineering tactic?',
                        'correct': 'Pretexting',
                        'options': 'Encryption,Firewall configuration,Pretexting,Software patching'
                    },
                    {
                        'question': 'What is tailgating in social engineering?',
                        'correct': 'Following someone through a secure door',
                        'options': 'Following someone through a secure door,Sending spam emails,Installing malware,Hacking passwords'
                    },
                    {
                        'question': 'How can you defend against baiting attacks?',
                        'correct': 'Never use unknown USB drives',
                        'options': 'Share all passwords,Never use unknown USB drives,Click all links,Trust everyone'
                    },
                    {
                        'question': 'What is a sign of a quid pro quo attack?',
                        'correct': 'Offering a service in exchange for sensitive information',
                        'options': 'Sending spam,Using encryption,Offering a service in exchange for sensitive information,Installing updates'
                    }
                ]
            elif topic.title == 'Mobile Device Security':
                questions = [
                    {
                        'question': 'What is a recommended mobile security practice?',
                        'correct': 'Enable device encryption',
                        'options': 'Share device passwords,Enable device encryption,Disable auto-lock,Use simple PINs'
                    },
                    {
                        'question': 'Where should you download mobile apps from?',
                        'correct': 'Official app stores',
                        'options': 'Any website,Third-party stores,Official app stores,Social media links'
                    },
                    {
                        'question': 'What should you do before connecting to public WiFi?',
                        'correct': 'Enable VPN',
                        'options': 'Share personal files,Enable VPN,Disable firewall,Turn off encryption'
                    },
                    {
                        'question': 'How often should you update your mobile apps?',
                        'correct': 'As soon as updates are available',
                        'options': 'Never,Once a year,As soon as updates are available,Only when not working'
                    },
                    {
                        'question': 'What is the best practice for mobile data backup?',
                        'correct': 'Regular automatic encrypted backups',
                        'options': 'Never backup,Share with friends,Regular automatic encrypted backups,Email to yourself'
                    }
                ]
            elif topic.title == 'Incident Response':
                questions = [
                    {
                        'question': 'What is the first step in incident response?',
                        'correct': 'Identification',
                        'options': 'Recovery,Containment,Identification,Eradication'
                    },
                    {
                        'question': 'What should you do during the containment phase?',
                        'correct': 'Isolate affected systems',
                        'options': 'Ignore the incident,Call the media,Isolate affected systems,Delete all files'
                    },
                    {
                        'question': 'During incident recovery, you should:',
                        'correct': 'Monitor systems for suspicious activity',
                        'options': 'Delete everything,Ignore warnings,Monitor systems for suspicious activity,Share passwords'
                    },
                    {
                        'question': 'What is important during incident documentation?',
                        'correct': 'Record all actions taken and their timestamps',
                        'options': 'Take photos only,Record all actions taken and their timestamps,Ignore small details,Call everyone'
                    },
                    {
                        'question': 'After an incident is resolved, you should:',
                        'correct': 'Conduct a lessons learned review',
                        'options': 'Forget about it,Conduct a lessons learned review,Blame others,Hide the evidence'
                    }
                ]
            else:  # Data Protection
                questions = []

            for q in questions:
                question = Question(
                    question_text=q['question'],
                    correct_answer=q['correct'],
                    options=q['options'],
                    topic_id=topic.id
                )
                db.session.add(question)

        db.session.commit()

if __name__ == '__main__':
    init_db()
