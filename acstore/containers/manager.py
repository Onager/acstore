# -*- coding: utf-8 -*-
"""This file contains the attribute container manager class."""


class AttributeContainersManager(object):
  """Class that implements the attribute container manager."""

  _attribute_container_classes = {}

  @classmethod
  def CreateAttributeContainer(cls, container_type):
    """Creates an instance of a specific attribute container type.

    Args:
      container_type (str): container type.

    Returns:
      AttributeContainer: an instance of attribute container.

    Raises:
      ValueError: if the container type is not supported.
    """
    container_class = cls._attribute_container_classes.get(
        container_type, None)
    if not container_class:
      raise ValueError(f'Unsupported container type: {container_type:s}')

    return container_class()

  @classmethod
  def DeregisterAttributeContainer(cls, attribute_container_class):
    """Deregisters an attribute container class.

    The attribute container classes are identified based on their lower case
    container type.

    Args:
      attribute_container_class (type): attribute container class.

    Raises:
      KeyError: if attribute container class is not set for the corresponding
          container type.
    """
    container_type = attribute_container_class.CONTAINER_TYPE.lower()
    if container_type not in cls._attribute_container_classes:
      raise KeyError((
          f'Attribute container class not set for container type: '
          f'{attribute_container_class.CONTAINER_TYPE:s}.'))

    del cls._attribute_container_classes[container_type]

  @classmethod
  def GetContainerTypes(cls):
    """Retrieves the container types of the registered attribute containers.

    Returns:
      list[str]: container types.
    """
    return list(cls._attribute_container_classes.keys())

  @classmethod
  def GetSchema(cls, container_type):
    """Retrieves the schema of a registered attribute container.

    Args:
      container_type (str): attribute container type.

    Returns:
      dict[str, str]: attribute container schema or an empty dictionary if
          no schema available.

    Raises:
      ValueError: if the container type is not supported.
    """
    container_class = cls._attribute_container_classes.get(
        container_type, None)
    if not container_class:
      raise ValueError(f'Unsupported container type: {container_type:s}')

    return getattr(container_class, 'SCHEMA', {})

  @classmethod
  def RegisterAttributeContainer(cls, attribute_container_class):
    """Registers a attribute container class.

    The attribute container classes are identified based on their lower case
    container type.

    Args:
      attribute_container_class (type): attribute container class.

    Raises:
      KeyError: if attribute container class is already set for the
          corresponding container type.
    """
    container_type = attribute_container_class.CONTAINER_TYPE.lower()
    if container_type in cls._attribute_container_classes:
      raise KeyError((
          f'Attribute container class already set for container type: '
          f'{attribute_container_class.CONTAINER_TYPE:s}.'))

    cls._attribute_container_classes[container_type] = attribute_container_class

  @classmethod
  def RegisterAttributeContainers(cls, attribute_container_classes):
    """Registers attribute container classes.

    The attribute container classes are identified based on their lower case
    container type.

    Args:
      attribute_container_classes (list[type]): attribute container classes.

    Raises:
      KeyError: if attribute container class is already set for the
          corresponding container type.
    """
    for attribute_container_class in attribute_container_classes:
      cls.RegisterAttributeContainer(attribute_container_class)
