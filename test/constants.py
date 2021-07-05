TEST_URL="https://age.api/api/"
TEST_VERSION="v1"
TEST_FULL_URL=TEST_URL+TEST_VERSION

AZTEC_RESULT={
  "id": 1,
  "name": "Aztecs",
  "expansion": "The Conquerors",
  "army_type": "Infantry and Monk",
  "unique_unit": [
    "https://age.api/api/v1/unit/jaguar_warrior"
  ],
  "unique_tech": [
    "https://age.api/api/v1/technology/garland_wars"
  ],
  "team_bonus": "Relics generate +33% gold",
  "civilization_bonus": [
    "Villagers carry +5",
    "Military units created 15% faster",
    "+5 Monk hit points for each Monastery technology",
    "Loom free"
  ]
}

GOTH_RESULT={
      "id": 7,
      "name": "Goths",
      "expansion": "Age of Kings",
      "army_type": "Infantry",
      "unique_unit": [
        "https://age.api/api/v1/unit/huskarl"
      ],
      "unique_tech": [
        "https://age.api/api/v1/technology/anarchy",
        "https://age.api/api/v1/technology/perfusion"
      ],
      "team_bonus": "Barracks operate 20% faster",
      "civilization_bonus": [
        "Infantry cost 35% less (starting in Feudal Age)",
        "Infantry have +1 attack against buildings",
        "Villagers have +5 attack versus wild boar",
        "Hunters carry +15 meat",
        "+10 to population limit in Imperial Age"
      ]
    }

KOREANS_RESULT={
      "id": 10,
      "name": "Koreans",
      "expansion": "The Conquerors",
      "army_type": "Tower and naval",
      "unique_unit": [
        "https://age.api/api/v1/unit/war_wagon",
        "https://age.api/api/v1/unit/turtle_ship"
      ],
      "unique_tech": [
        "https://age.api/api/v1/technology/shinkichon"
      ],
      "team_bonus": "Mangonel line has +1 range",
      "civilization_bonus": [
        "Villagers have +3 line of sight",
        "Stone miners work 20% faster",
        "Guard Tower and Keep upgrades are free",
        "Towers (except bombard towers) have +1 range in Castle Age/ +2 in Imperial Age"
      ]
    }

KHMER_RESULT={
      "id": 27,
      "name": "Khmer",
      "expansion": "Rise of Rajas",
      "army_type": "Siege and Elephant Civilzation",
      "unique_unit": [],
      "unique_tech": [],
      "team_bonus": "Scorpions have +1 range",
      "civilization_bonus": [
        "Prereq buildings aren't required to advance to further ages or unlock other buildings",
        "Battle Elephants are +15% faster",
        "Villagers can garrison in Houses"
      ]
    }

NO_UNIT_RESULT=    {
      "unique_unit": []
}

NO_TECH_RESULT={
      "unique_tech": []
}

EAGLE_WARRIOR_RESULT={
  "id": 9,
  "name": "Eagle Warrior",
  "description": "Fast infantry with extensive sight; resists conversion; attack bonus vs. Monks",
  "expansion": "The Conquerors",
  "age": "Dark",
  "created_in": "https://age.api/api/v1/structure/barracks",
  "cost": {
    "info": "1 Unit free at the start of the game for Aztecs and Mayans"
  },
  "reload_time": 2,
  "movement_rate": 1.1,
  "line_of_sight": 6,
  "hit_points": 50,
  "attack": 4,
  "armor": "0/2",
  "attack_bonus": [
    "+8 monks",
    "+3 siege"
  ]
}

JAGUAR_WARRIOR_RESULT={
  "id": 79,
  "name": "Jaguar Warrior",
  "description": "Aztec unique unit. Attack bonus vs. other infantry",
  "expansion": "The Conquerors",
  "age": "Castle",
  "created_in": "https://age.api/api/v1/structure/castle",
  "cost": {
    "Food": 60,
    "Gold": 30
  },
  "build_time": 17,
  "reload_time": 2,
  "movement_rate": 1,
  "line_of_sight": 3,
  "hit_points": 50,
  "attack": 10,
  "armor": "1/0",
  "attack_bonus": [
    "+12 eagles",
    "+2 buildings",
    "+10 infantry"
  ]
}

WAR_WAGON_RESULT={
  "id": 101,
  "name": "War Wagon",
  "description": "Korean unique unit. Heavily armored horse-drawn archery unit",
  "expansion": "The Conquerors",
  "age": "Castle",
  "created_in": "https://age.api/api/v1/structure/castle",
  "cost": {
    "Wood": 120,
    "Gold": 60
  },
  "build_time": 25,
  "reload_time": 2.5,
  "attack_delay": 1,
  "movement_rate": 1.2,
  "line_of_sight": 6,
  "hit_points": 150,
  "range": 4,
  "attack": 9,
  "armor": "0/3",
  "attack_bonus": [
    "+5 buildings"
  ],
  "search_radius": 6,
  "accuracy": "100%"
}

TURTLE_SHIP_RESULT={
  "id": 38,
  "name": "Turtle Ship",
  "description": "Korean unique unit. Slow and ironclad battleship used to destroy other ships at close range",
  "expansion": "The Conquerors",
  "age": "Castle",
  "created_in": "https://age.api/api/v1/structure/dock",
  "cost": {
    "Wood": 200,
    "Gold": 200
  },
  "build_time": 50,
  "reload_time": 6,
  "movement_rate": 0.9,
  "line_of_sight": 8,
  "hit_points": 200,
  "range": 6,
  "attack": 50,
  "armor": "6/5",
  "armor_bonus": [
    "+8 ships"
  ],
  "blast_radius": 0.5
}

HUSKARL_RESULT={
  "id": 77,
  "name": "Huskarl",
  "description": "Gothic unique unit. Infantry with substantial pierce armor; virtually immune to archer fire. Attack bonus vs. buildings and archers",
  "expansion": "Age of Kings",
  "age": "Castle",
  "created_in": "https://age.api/api/v1/structure/castle",
  "cost": {
    "Food": 52,
    "Gold": 26
  },
  "build_time": 16,
  "reload_time": 2,
  "movement_rate": 1.05,
  "line_of_sight": 3,
  "hit_points": 60,
  "attack": 10,
  "armor": "0/6",
  "attack_bonus": [
    "+2 eagles",
    "+2 buildings",
    "+6 archers/hand cannoneers"
  ]
}

BARRACKS_RESULT=[
  {
    "id": 1,
    "name": "Barracks",
    "expansion": "Age of Kings",
    "age": "Dark",
    "cost": {
      "Wood": 175
    },
    "build_time": 50,
    "hit_points": 1200,
    "line_of_sight": 5,
    "armor": "0/7",
    "special": [
      "Garrison: 10 created units"
    ]
  },
  {
    "id": 11,
    "name": "Barracks",
    "expansion": "Age of Kings",
    "age": "Feudal",
    "cost": {
      "Wood": 175
    },
    "build_time": 50,
    "hit_points": 1500,
    "line_of_sight": 5,
    "armor": "1/8",
    "special": [
      "Garrison: 10 created units"
    ]
  },
  {
    "id": 22,
    "name": "Barracks",
    "expansion": "Age of Kings",
    "age": "Castle",
    "cost": {
      "Wood": 175
    },
    "build_time": 50,
    "hit_points": 1800,
    "line_of_sight": 5,
    "armor": "2/9",
    "special": [
      "Garrison: 10 created units"
    ]
  },
  {
    "id": 37,
    "name": "Barracks",
    "expansion": "Age of Kings",
    "age": "Imperial",
    "cost": {
      "Wood": 175
    },
    "build_time": 50,
    "hit_points": 2100,
    "line_of_sight": 5,
    "armor": "3/10",
    "special": [
      "Garrison: 10 created units"
    ]
  }
]

HERESY_RESULT={
  "id": 65,
  "name": "Heresy",
  "description": "Converted units die",
  "expansion": "Age of Kings",
  "age": "Castle",
  "develops_in": "https://age.api/api/v1/structure/monastery",
  "cost": {
    "Gold": 1000
  },
  "build_time": 60,
  "applies_to": [
    "Monks"
  ]
}

ANARCHY_RESULT={
  "id": 104,
  "name": "Anarchy",
  "description": "Allow the creation of Huskarls in barracks",
  "expansion": "Age of Kings",
  "age": "Castle",
  "develops_in": "https://age.api/api/v1/structure/castle",
  "cost": {
    "Food": 450,
    "Gold": 250
  },
  "build_time": 60,
  "applies_to": [
    "https://age.api/api/v1/civilization/goths"
  ]
}

PERFUSION_RESULT={
  "id": 117,
  "name": "Perfusion",
  "description": "Barracks working rate * 2 (unit creation time halved)",
  "expansion": "Age of Kings",
  "age": "Imperial",
  "develops_in": "https://age.api/api/v1/structure/castle",
  "cost": {
    "Food": 400,
    "Gold": 600
  },
  "build_time": 40,
  "applies_to": [
    "https://age.api/api/v1/civilization/goths",
    "https://age.api/api/v1/structure/barracks"
  ]
}

GARLAND_WARS_RESULT={
  "id": 113,
  "name": "Garland Wars",
  "description": "Infantry +4 attack",
  "expansion": "The Conquerors",
  "age": "Imperial",
  "develops_in": "https://age.api/api/v1/structure/castle",
  "cost": {
    "Food": 450,
    "Gold": 750
  },
  "build_time": 60,
  "applies_to": [
    "https://age.api/api/v1/civilization/aztecs"
  ]
}

UNIQUE_UNIT_INPUT_SINGLE={
  "unique_unit": [
    "https://age.api/api/v1/unit/eagle_warrior"
  ]
}

UNIQUE_UNIT_INPUT_MULTIPLE={
  "unique_unit": [
      "https://age.api/api/v1/unit/war_wagon",
      "https://age.api/api/v1/unit/turtle_ship"
  ]
}

UNIQUE_TECH_INPUT_SINGLE={
  "unique_unit": [
    "https://age.api/api/v1/techonoloy/garland_wars",
  ]
}

UNIQUE_TECH_INPUT_MULTIPLE={
    "unique_tech": [
      "https://age.api/api/v1/technology/anarchy",
      "https://age.api/api/v1/technology/perfusion"
    ]
}