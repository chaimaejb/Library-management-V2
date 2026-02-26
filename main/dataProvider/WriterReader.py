from pathlib import Path
import json
from mappers.BookMapper import BookMapper
from mappers.DVDMapper import DVDMapper
from mappers.MemberMapper import MemberMapper

class WriterReader:

  MAPPER_MAP = {
    "Book": BookMapper,
    "ReferenceBook": BookMapper,
    "DVD": DVDMapper,
    "Member": MemberMapper,
  }

  @staticmethod
  def get_file_path(filename):
    file_path = Path("data") / filename  # Create a path that points to a file named filename inside the data folder (data/filename) #  It does NOT create the folder # file_path type is not str
    if not file_path.parent.exists():  # .parent gives the folder containing the file (data)
      file_path.parent.mkdir(parents=True)  # .mkdir() creates a new folder. parent = true : If data don’t exist, Python will create it automatically
    return file_path
  
  @staticmethod
  def write(filename, data):
    file_path = WriterReader.get_file_path(filename)
    with open(file_path, "w") as f:
      json.dump(data, f)

  @staticmethod
  def read(filename):
    file_path = WriterReader.get_file_path(filename)

    try:
      with open(file_path, "r") as f:
        data = json.load(f)
    except FileNotFoundError:
      return []
    return data

  @staticmethod
  def save(obj, cls_name, filename):  # We load saved existing data and we add the new one then we re-write it
  
    data = WriterReader.read(filename)

    mapper = WriterReader.MAPPER_MAP.get(cls_name)
    if not mapper:
      raise ValueError(f"Unknown class name: {cls_name}")
    
    data.append(mapper.to_dict(obj))

    WriterReader.write(filename, data)

  @staticmethod
  def load_all(cls_name, filename):
    data = WriterReader.read(filename)

    mapper = WriterReader.MAPPER_MAP.get(cls_name)
    if not mapper:
      raise ValueError(f"Unknown class name: {cls_name}")

    return [mapper.from_dict(d) for d in data]
  
  @staticmethod
  def remove(obj, filename):
    file_path = WriterReader.get_file_path(filename)

    data = WriterReader.read(filename)
    if not data:
      print("data vide")
      return

    for i, d in enumerate(data):     # for large data need update, we can affect pointers to each id and del data[pointer]
      if d["id"] == obj.id:
        del data[i]
        break

    WriterReader.write(filename, data)
  
  @staticmethod
  def update(obj, cls_name, filename):
    mapper = WriterReader.MAPPER_MAP.get(cls_name)
    if not mapper:
      raise ValueError(f"Unknown class name: {cls_name}")
    
    data = WriterReader.read(filename)
    for i, d in enumerate(data):
      if d["id"] == obj.id:
        data[i] = mapper.to_dict(obj)
        break
    WriterReader.write(filename, data)

  