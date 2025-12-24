# Skeletal Campaign Orchestrator - Modular Parts

This directory contains the modular components of the Skeletal Campaign Orchestrator v1.0, broken into logical sections for easier editing and maintenance.

## 📁 Directory Structure

```
skeleton_orchestrator_parts/
├── assemble_orchestrator.py          # Assembly script
├── README.md                          # This file
├── orchestrator_header.md             # Title and critical dependency warning
├── section_0_framework_principles.md  # Core design philosophy
├── section_1_campaign_skeleton.md     # Campaign structure template
├── section_2_world_rules.md          # Faction, economy, magic, combat rules
├── section_3_character_templates.md  # NPC and companion templates
├── section_4_encounter_framework.md  # Encounter trigger templates
├── section_5_decision_points.md      # Decision point framework
├── section_6_world_state_tracking.md # State flags and reputation tracking
├── section_7_session_prep.md         # Pre-session checklist
├── section_8_dm_reasoning.md         # DM reasoning protocol
├── section_8_5_context_weaving.md    # Context weaving system (CRITICAL)
├── section_9_save_file_format.md     # Minimal state export format
├── section_10_orchestrator_integration.md  # Integration with D&D 5E orchestrator
├── section_11_example_campaign.md    # Example: The Shattered Court
├── section_12_usage_notes.md         # How to use this framework
├── section_13_migration_notes.md     # Converting comprehensive campaigns
└── orchestrator_footer.md            # Metadata and end marker
```

## 🔧 Usage

### Assemble Complete Orchestrator

```bash
python assemble_orchestrator.py
```

This creates `SKELETAL_CAMPAIGN_ORCHESTRATOR_v1_0.md` in the parent directory.

### Assembly Options

```bash
# Custom output filename
python assemble_orchestrator.py --output MY_ORCHESTRATOR.md

# Validate parts without assembling
python assemble_orchestrator.py --validate

# Generate with table of contents
python assemble_orchestrator.py --toc
```

## 📝 Editing Workflow

1. **Edit individual section files** - Make changes to specific sections as needed
2. **Run assembly script** - Regenerate the complete orchestrator
3. **Test with AI DM** - Verify changes work as expected

## 📊 File Sizes

- **Header**: ~1.1 KB
- **Section 0**: ~1.5 KB (Framework Principles)
- **Section 0.5**: ~13.4 KB (IP-Clean Framework - **NEW!**)
- **Section 1**: ~0.4 KB (Campaign Skeleton)
- **Section 2**: ~2.1 KB (World Rules)
- **Section 3**: ~1.4 KB (Character Templates)
- **Section 4**: ~1.1 KB (Encounter Framework)
- **Section 5**: ~1.0 KB (Decision Points)
- **Section 6**: ~0.8 KB (World State Tracking)
- **Section 7**: ~0.4 KB (Session Prep)
- **Section 8**: ~0.5 KB (DM Reasoning)
- **Section 8.5**: ~7.1 KB (Context Weaving - **LARGEST SECTION**)
- **Section 9**: ~0.7 KB (Save File Format)
- **Section 10**: ~1.4 KB (Orchestrator Integration)
- **Section 11**: ~1.8 KB (Example Campaign)
- **Section 12**: ~0.4 KB (Usage Notes)
- **Section 13**: ~0.6 KB (Migration Notes)
- **Footer**: ~1.5 KB

**Total Assembled**: ~38 KB (1,139 lines)

## 🎯 Key Sections Explained

### Critical Dependencies (Header)
- Explains why context weaving is non-negotiable
- Sets expectations for skeletal campaign requirements

### Section 0.5: IP-Clean Framework 🆕 IMPORTANT
**Second largest section at 13.4 KB** - Essential for source-inspired campaigns. Contains:
- Archetype pointer system (no copyrighted content stored)
- AI rendering directives for authentic experiences
- Trade dress protection guidelines
- Campaign metadata format
- Legal attribution templates
- Complete IP-clean campaign template

**Use when:** Your campaign draws inspiration from existing fictional universes (Dragonlance, Forgotten Realms, Star Wars, etc.)

### Section 8.5: Context Weaving ⚠️ CRITICAL
**Largest section at 7.1 KB** - This is the load-bearing component that prevents skeletal campaigns from becoming incoherent. Contains:
- TIER 0-4 context weaving protocols
- State validation before every output
- Context weaving for different scenarios (combat, negotiation, exploration, social)
- Integration requirements

### Section 2: World Rules
**Second largest at 2.1 KB** - Contains templates for:
- Faction mechanics and reputation math
- Economy and resource systems
- Magic system rules
- Combat difficulty scaling

### Section 11: Example Campaign
**1.8 KB** - Concrete example "The Shattered Court" showing how to use the framework in practice.

## 🔄 Assembly Process

The script combines files in this order:

1. Assembly header (auto-generated timestamp)
2. Orchestrator header (critical warnings)
3. Sections 0-13 (in numerical order)
4. Footer (metadata)

Each section is separated by blank lines for readability.

## ⚙️ Maintenance

When updating the orchestrator:

1. **Small changes**: Edit the specific section file directly
2. **Structural changes**: Update multiple sections as needed
3. **Version updates**: Update `ORCHESTRATOR_VERSION` in `assemble_orchestrator.py`
4. **New sections**: Add to `PARTS` list in `assemble_orchestrator.py`

## 🎮 Integration

The assembled orchestrator integrates with:
- **CORE_DND5E_AGENT_ORCHESTRATOR_v6_8_0**
- **Player Agency protocols**
- **Decision Point Framework**
- **Ambient Context Weaving (TIER 0-4)**

## 📖 Design Philosophy

**Skeletal campaigns specify 20%, let 80% emerge:**
- ✅ World rules and feedback loops
- ✅ Character motivations and constraints
- ✅ Consequence chains and reputation math
- ❌ Pre-written dialogue
- ❌ Detailed location descriptions
- ❌ Quest branches
- ❌ Predetermined outcomes

## 🚀 Next Steps

After assembling:
1. Use the orchestrator as a template for building campaigns
2. Fill in Sections 1-6 with your campaign specifics
3. Reference Sections 7-13 during gameplay and session prep
4. Trust the context weaving system to maintain coherence

---

**Version**: 1.0
**Status**: Template Ready
**Purpose**: Enable AI-driven emergent gameplay through minimal specification and explicit feedback loops
