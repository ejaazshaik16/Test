import json

with open("resume.json") as f:
    data = json.load(f)

lines = []
lines.append(f"# {data['name']}")
lines.append(f"**{data['title']}**\n")
lines.append(f"- Email: {data['contact']['email']}")
lines.append(f"- Phone: {data['contact']['phone']}")
lines.append(f"- LinkedIn: [{data['contact']['linkedin']}]({data['contact']['linkedin']})")
lines.append(f"- GitHub: [{data['contact']['github']}]({data['contact']['github']})\n")
lines.append(f"## Summary\n{data['summary']}\n")

lines.append("## Skills")
lines.append(", ".join(data["skills"]) + "\n")

lines.append("## Tools & Software")
lines.append(", ".join(data["tools_and_software"]) + "\n")

lines.append("## Certifications")
lines.append(", ".join(data["certifications"]) + "\n")

lines.append("## Experience")
for exp in data["work_experience"]:
    lines.append(f"**{exp['role']}**, {exp['company']}, {exp['location']} ({exp['dates']})")
    lines.append(f"- {exp['responsibilities']}\n")

lines.append("## Education")
for edu in data["education"]:
    lines.append(f"**{edu['degree']}**, {edu['institution']}, {edu['location']} ({edu['dates']})\n")

with open("README.md", "w") as f:
    f.write("\n".join(lines))

print("✅ Markdown resume generated in README.md")
