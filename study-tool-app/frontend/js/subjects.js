const subjects = [
    {
        name: "Math",
        topics: [
            "Algebra",
            "Geometry",
            "Calculus",
            "Statistics"
        ],
        resources: [
            {
                title: "Khan Academy - Math",
                url: "https://www.khanacademy.org/math"
            },
            {
                title: "Math is Fun",
                url: "https://www.mathsisfun.com/"
            }
        ]
    },
    {
        name: "English",
        topics: [
            "Grammar",
            "Literature",
            "Writing",
            "Vocabulary"
        ],
        resources: [
            {
                title: "Grammarly",
                url: "https://www.grammarly.com/"
            },
            {
                title: "Purdue OWL",
                url: "https://owl.purdue.edu/"
            }
        ]
    },
    {
        name: "Biology",
        topics: [
            "Cell Biology",
            "Genetics",
            "Evolution",
            "Ecology"
        ],
        resources: [
            {
                title: "Khan Academy - Biology",
                url: "https://www.khanacademy.org/science/biology"
            },
            {
                title: "Biology Online",
                url: "https://www.biologyonline.com/"
            }
        ]
    },
    {
        name: "Accounting",
        topics: [
            "Financial Accounting",
            "Managerial Accounting",
            "Tax Accounting",
            "Auditing"
        ],
        resources: [
            {
                title: "AccountingCoach",
                url: "https://www.accountingcoach.com/"
            },
            {
                title: "Investopedia - Accounting",
                url: "https://www.investopedia.com/accounting-4427765"
            }
        ]
    },
    {
        name: "Physics",
        topics: [
            "Classical Mechanics",
            "Thermodynamics",
            "Electromagnetism",
            "Quantum Physics"
        ],
        resources: [
            {
                title: "Physics Classroom",
                url: "https://www.physicsclassroom.com/"
            },
            {
                title: "HyperPhysics",
                url: "http://hyperphysics.phy-astr.gsu.edu/"
            }
        ]
    },
    {
        name: "Chemistry",
        topics: [
            "Organic Chemistry",
            "Inorganic Chemistry",
            "Physical Chemistry",
            "Analytical Chemistry"
        ],
        resources: [
            {
                title: "ChemCollective",
                url: "http://chemcollective.org/"
            },
            {
                title: "Khan Academy - Chemistry",
                url: "https://www.khanacademy.org/science/chemistry"
            }
        ]
    },
    {
        name: "Literature",
        topics: [
            "Poetry",
            "Prose",
            "Drama",
            "Literary Analysis"
        ],
        resources: [
            {
                title: "Poetry Foundation",
                url: "https://www.poetryfoundation.org/"
            },
            {
                title: "Project Gutenberg",
                url: "https://www.gutenberg.org/"
            }
        ]
    },
    {
        name: "Economics",
        topics: [
            "Microeconomics",
            "Macroeconomics",
            "International Economics",
            "Development Economics"
        ],
        resources: [
            {
                title: "Investopedia - Economics",
                url: "https://www.investopedia.com/economics-4427766"
            },
            {
                title: "Khan Academy - Economics",
                url: "https://www.khanacademy.org/economics-finance-domain"
            }
        ]
    },
    {
        name: "Civic Education",
        topics: [
            "Government Structure",
            "Rights and Responsibilities",
            "Civic Participation",
            "Current Events"
        ],
        resources: [
            {
                title: "Civics 101",
                url: "https://www.civics101.org/"
            },
            {
                title: "iCivics",
                url: "https://www.icivics.org/"
            }
        ]
    },
    {
        name: "Government",
        topics: [
            "Political Systems",
            "Public Policy",
            "International Relations",
            "Political Theory"
        ],
        resources: [
            {
                title: "GovTrack",
                url: "https://www.govtrack.us/"
            },
            {
                title: "Ballotpedia",
                url: "https://ballotpedia.org/"
            }
        ]
    },
    {
        name: "Geography",
        topics: [
            "Physical Geography",
            "Human Geography",
            "Geographical Information Systems",
            "Cultural Geography"
        ],
        resources: [
            {
                title: "National Geographic",
                url: "https://www.nationalgeographic.com/"
            },
            {
                title: "Geography Now",
                url: "https://www.geographynow.com/"
            }
        ]
    },
    {
        name: "Design",
        topics: [
            "Graphic Design",
            "Web Design",
            "Product Design",
            "User Experience Design"
        ],
        resources: [
            {
                title: "Canva Design School",
                url: "https://www.canva.com/designschool/"
            },
            {
                title: "Adobe Creative Cloud Tutorials",
                url: "https://helpx.adobe.com/creative-cloud/tutorials.html"
            }
        ]
    }
];

function getSubjects() {
    return subjects;
}

function getSubjectDetails(subjectName) {
    return subjects.find(subject => subject.name.toLowerCase() === subjectName.toLowerCase());
}

export { getSubjects, getSubjectDetails };