# Day 2: MCP Server — RoshniAI University Data Provider
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("RoshniAI-MCP-Server")

@mcp.tool()
def get_universities(country: str, field: str, budget: int) -> str:
    """MCP Tool: Get universities by country, field and budget"""
    universities = {
        "turkey": [
            {"name": "Bogazici University", "ranking": "501-600", "tuition": 3000, "field": "Computer Science"},
            {"name": "METU", "ranking": "601-800", "tuition": 4000, "field": "Computer Science"},
            {"name": "Bilkent University", "ranking": "501-600", "tuition": 3500, "field": "Computer Science"},
            {"name": "Sabanci University", "ranking": "801-1000", "tuition": 4500, "field": "Computer Science"},
            {"name": "Koc University", "ranking": "401-500", "tuition": 5000, "field": "Computer Science"},
        ],
        "malaysia": [
            {"name": "University of Malaya", "ranking": "301-350", "tuition": 4200, "field": "Computer Science"},
            {"name": "UTM", "ranking": "401-450", "tuition": 3800, "field": "Computer Science"},
            {"name": "Taylor's University", "ranking": "401-450", "tuition": 4500, "field": "Computer Science"},
            {"name": "Monash Malaysia", "ranking": "351-400", "tuition": 5000, "field": "Computer Science"},
            {"name": "UPM", "ranking": "401-450", "tuition": 3500, "field": "Computer Science"},
        ],
        "pakistan": [
            {"name": "LUMS", "ranking": "701-750", "tuition": 2000, "field": "Computer Science"},
            {"name": "NUST", "ranking": "601-650", "tuition": 1500, "field": "Computer Science"},
            {"name": "COMSATS", "ranking": "701-750", "tuition": 1200, "field": "Computer Science"},
            {"name": "IBA Karachi", "ranking": "701-750", "tuition": 1800, "field": "Computer Science"},
            {"name": "FAST NUCES", "ranking": "701-750", "tuition": 1600, "field": "Computer Science"},
        ],
        "usa": [
            {"name": "MIT", "ranking": "1", "tuition": 55000, "field": "Computer Science"},
            {"name": "Stanford", "ranking": "3", "tuition": 56000, "field": "Computer Science"},
            {"name": "Carnegie Mellon", "ranking": "25", "tuition": 58000, "field": "Computer Science"},
            {"name": "UC Berkeley", "ranking": "10", "tuition": 44000, "field": "Computer Science"},
            {"name": "Harvard", "ranking": "5", "tuition": 54000, "field": "Computer Science"},
        ],
        "uk": [
            {"name": "Oxford", "ranking": "3", "tuition": 35000, "field": "Computer Science"},
            {"name": "Cambridge", "ranking": "2", "tuition": 33000, "field": "Computer Science"},
            {"name": "Imperial College", "ranking": "6", "tuition": 38000, "field": "Computer Science"},
            {"name": "UCL", "ranking": "9", "tuition": 32000, "field": "Computer Science"},
            {"name": "Edinburgh", "ranking": "22", "tuition": 28000, "field": "Computer Science"},
        ]
    }
    
    country_lower = country.lower()
    results = universities.get(country_lower, [])
    filtered = [u for u in results if u["tuition"] <= budget]
    
    if not filtered:
        filtered = results
    
    output = f"🎓 Universities in {country} for {field}:\n\n"
    for i, u in enumerate(filtered[:5], 1):
        output += f"{i}. {u['name']}\n"
        output += f"   • Ranking: {u['ranking']}\n"
        output += f"   • Tuition: ${u['tuition']}/year\n\n"
    
    return output

@mcp.tool()
def get_scholarships(country: str, grades: str) -> str:
    """MCP Tool: Get scholarships by country and grades"""
    scholarships = {
        "turkey": [
            "🏆 Türkiye Scholarships — Fully funded (tuition + living + flights)",
            "🎓 YTB Scholarship — Full tuition + monthly stipend",
            "📚 Bilkent Merit Scholarship — Full tuition waiver",
            "🌟 Koc University Scholarship — Full tuition + accommodation",
            "💡 Sabanci Excellence Scholarship — Partial tuition (75%)",
        ],
        "malaysia": [
            "🏆 Malaysia International Scholarship — Fully funded",
            "🎓 Khazanah Scholarship — Full tuition + living allowance",
            "📚 ASEAN Scholarship — Partial funding",
            "🌟 Taylor's Excellence Award — 50% tuition waiver",
            "💡 Monash International Merit — Partial scholarship",
        ],
        "pakistan": [
            "🏆 HEC Need Based Scholarship — Full tuition",
            "🎓 LUMS National Outreach — Full funding for deserving students",
            "📚 NUST Merit Scholarship — Full tuition waiver",
            "🌟 COMSATS Excellence Award — 50% tuition",
            "💡 Prime Minister Laptop Scheme — Laptop + support",
        ],
        "usa": [
            "🏆 Fulbright Scholarship — Fully funded for international students",
            "🎓 Gates Cambridge — Full funding",
            "📚 Knight-Hennessy (Stanford) — Full funding",
            "🌟 MIT Fellowship — Full tuition + stipend",
            "💡 Carnegie Mellon Merit — Partial funding",
        ]
    }
    
    country_lower = country.lower()
    results = scholarships.get(country_lower, [
        "🏆 Check official university websites for scholarships",
        "🎓 Look for government bilateral scholarships",
        "📚 Search for field-specific international scholarships"
    ])
    
    output = f"💰 Scholarships for {country} (Grades: {grades}):\n\n"
    for s in results:
        output += f"  {s}\n"
    
    return output

@mcp.tool()  
def get_career_paths(field: str) -> str:
    """MCP Tool: Get career paths for a field of study"""
    careers = {
        "computer science": [
            "💻 Software Engineer — Average salary $120,000/year",
            "🤖 AI/ML Engineer — Average salary $140,000/year", 
            "🔒 Cybersecurity Analyst — Average salary $110,000/year",
            "☁️ Cloud Architect — Average salary $130,000/year",
            "📊 Data Scientist — Average salary $125,000/year",
        ],
        "medicine": [
            "👨‍⚕️ General Physician — Average salary $200,000/year",
            "🔬 Medical Researcher — Average salary $90,000/year",
            "🏥 Hospital Administrator — Average salary $100,000/year",
        ],
        "business": [
            "📈 Investment Banker — Average salary $150,000/year",
            "🏢 Management Consultant — Average salary $120,000/year",
            "🚀 Entrepreneur — Unlimited potential",
        ]
    }
    
    field_lower = field.lower()
    results = careers.get(field_lower, [
        "🔍 Research career opportunities in your field",
        "💼 Connect with professionals on LinkedIn",
        "📚 Look for internship opportunities"
    ])
    
    output = f"🚀 Career Paths for {field}:\n\n"
    for c in results:
        output += f"  {c}\n"
    
    return output

if __name__ == "__main__":
    print("🚀 RoshniAI MCP Server Starting...")
    print("✅ MCP Tools Ready: get_universities, get_scholarships, get_career_paths")
    mcp.run()