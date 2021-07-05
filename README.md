# python-aoe2
https://pypi.org/project/pythonaoe2/

## How to Use:

### Import the library:
```python
>>> from pythonaoe2 import aoe2
```

### Initialize the Client:
```python
>>> client = aoe2.Client()
```

Or if you are running your own instance of the api:

```python
>>> client = aoe2.Client("https://your.url.here/"+"api_version")
```

### Get Civilizations:
```python
>>> client.get_all_civilizations()
```

Civilizations are returned as objects:

```python
>>> for civ in client.get_all_civilizations():
>>>     print(civ.name)
Aztecs
...
Vietnamese
```

### Get a Civilization by ID or Name:
```python
>>> client.get_civilization("Aztecs").name
'Aztecs'
>>> client.get_civilization("1").name      
'Aztecs'
>>> 
```

### Get all Units:
```python
>>> for unit in client.get_all_units(): 
>>>     print(unit.name)                  
Archer
...
Elite Woad Raider
```

### Get a Unit by ID or Name:
```python
>>> client.get_unit("1").name 
'Archer'
>>> client.get_unit("Archer").name
'Archer'
```

### Get all structures:
```python
>>> for structure in client.get_all_structures():)  d))
>>>     print(structure.name + "|" + str(structure.id))
Barracks|1
...
Keep|59
>>>
```

### Get Structure by Name or ID:
```python
>>> client.get_structure("59").name
'Keep'
>>> client.get_structure("Keep").name
'Keep'
```

### Get all Technologies:
```python
>>> for tech in client.get_all_technologies(): 
>>>     print(tech.name)
Crossbowman
...
Elite Woad Raider
```

### Get Technology by ID or Name:
```python
>>> client.get_technology("1").name
'Crossbowman'
>>> client.get_technology("Crossbowman").name 
'Crossbowman'
```

### Other Notes:
Some information requires additonal API calls with the provided ID/Name values, and some structures have multiple entries for different ages:

```python
>>> unit = client.get_unit("4")                   
>>> unit.name
'Cavalry Archer'
>>> for structure in client.get_structure(unit.created_in):
>>>     print(structure.name + " | " + structure.age) 
Archery Range | Feudal
Archery Range | Castle
Archery Range | Imperial
```

```python
>>> tech = client.get_technology("3") 
>>> tech.applies_to
['crossbowman']
>>> tech.develops_in
'archery_range'
>>> unit = client.get_unit(tech.applies_to[0])
>>> unit.name
'Crossbowman'
```
