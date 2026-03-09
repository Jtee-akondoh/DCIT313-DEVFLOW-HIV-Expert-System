# HIV/AIDS Expert System - Knowledge Engineering Report

## Group Members
- [Name 1] - [Student ID] - Role: Knowledge Base Developer
- [Name 2] - [Student ID] - Role: Interface Developer  
- [Name 3] - [Student ID] - Role: Documentation & Testing

## System Purpose
This expert system provides information about HIV/AIDS and assists users in understanding risk factors and symptoms. It demonstrates how symbolic AI can be used to encode medical knowledge into logical rules.

## Knowledge Sources
1. World Health Organization (WHO) - HIV/AIDS Fact Sheets
2. Centers for Disease Control and Prevention (CDC) - HIV Basics
3. UNAIDS - Global HIV Statistics
4. Peer-reviewed medical literature on HIV transmission and symptoms

## Knowledge Engineering Process

### 1. Knowledge Acquisition
- Gathered information from authoritative medical sources
- Identified key concepts: transmission methods, prevention, symptoms, risk factors
- Structured information into logical categories

### 2. Knowledge Representation
- **Facts**: Basic statements about HIV (transmission methods, symptoms)
- **Rules**: Logical relationships for risk assessment and advice generation
- **Dynamic Facts**: User inputs that change during consultation

### 3. Rule Development
- Risk levels determined by combinations of risk factors
- Symptom analysis based on number and type of symptoms
- Information provision based on user queries

## System Architecture
User Input → Python Interface → Prolog Knowledge Base → Inference → Output
↑ |
└─────────────────── Feedback Loop ──────────────────────────┘

## Testing
### Positive Test Cases
1. User with multiple risk factors → High risk recommendation
2. User with 3+ early symptoms → Testing suggested
3. User asking about transmission → Correct information provided

### Negative Test Cases
1. User with no risk factors → Low risk/unknown
2. User with 1-2 symptoms → General advice only
3. Invalid inputs → Proper error handling

## Limitations
- Not a diagnostic tool
- Limited to basic HIV/AIDS knowledge
- Cannot replace professional medical advice
- Symptoms may overlap with other conditions

## Future Improvements
- Add more detailed risk calculation algorithms
- Include geographic-specific resources
- Add multilingual support
- Implement machine learning for better symptom analysis