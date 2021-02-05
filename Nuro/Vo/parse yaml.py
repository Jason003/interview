import collections
class YAML_Parser:
    def __init__(self, yaml):
        self.dic = self.parse_yaml(yaml)
        self.parse_yaml(yaml)

    def get(self, q):
        return self.dic.get(q, None)

    def parse_yaml(self, yaml):

        def get_kv(line):
            idx = line.find(':')
            return line[:idx], line[idx + 1:]

        lines = yaml.split('\n')
        indent = {i: lines[i].find('k') for i in range(len(lines))}
        kvs = [get_kv(s.strip()) for s in lines]
        parent = {}
        candidate = set()
        res = {}
        for i in range(len(lines) - 1, -1, -1):
            toRemove = set()
            for c in candidate:
                if indent[c] > indent[i]:
                    toRemove.add(c)
                    parent[c] = i
            candidate -= toRemove
            candidate.add(i)
        for i, kv in enumerate(kvs):
            if kv[1]:
                path = [i]
                while path[-1] in parent:
                    path.append(parent[path[-1]])
                res['.'.join(kvs[i][0] for i in reversed(path))] = kv[1]
        return res
s = '''k1:v1
k2:
  k21:v2
  k22:
             k211:v211:::
  k23:
      k231:v231
k3:v3'''
print(YAML_Parser(s).dic)

